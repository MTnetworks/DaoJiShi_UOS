#!/bin/bash
set -e

# Define paths
WORK_DIR=$(pwd)
BUILD_DIR="${WORK_DIR}/dist_deb_build"
PACKAGE_DIR="${BUILD_DIR}/deb_package"

echo "=== DaoJiShi UOS Packaging Script ==="

# 0. Detect Architecture
ARCH=$(dpkg --print-architecture 2>/dev/null || echo "amd64")
echo "Detected Architecture: $ARCH"

# 1. Check Dependencies
echo "[1/5] Checking environment dependencies..."
if ! python3 uos_packaging/check_env.py; then
    echo "Environment check failed. Please fix dependencies and try again."
    exit 1
fi

# 2. Install PyInstaller if missing
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi

# 3. Skip PyInstaller Build
echo "[2/5] Skipping PyInstaller build (using source mode)..."

# 4. Prepare DEB Directory Structure
echo "[3/5] Creating DEB package structure..."
rm -rf "${BUILD_DIR}"
mkdir -p "${PACKAGE_DIR}/DEBIAN"
mkdir -p "${PACKAGE_DIR}/opt/DaoJiShi"
mkdir -p "${PACKAGE_DIR}/usr/share/applications"
# Create standard icon directory
mkdir -p "${PACKAGE_DIR}/usr/share/icons/hicolor/256x256/apps"

# 5. Copy Files
echo "[4/5] Copying source files..."
# Copy source code
cp -r app "${PACKAGE_DIR}/opt/DaoJiShi/"
cp run.py "${PACKAGE_DIR}/opt/DaoJiShi/"
cp config.json "${PACKAGE_DIR}/opt/DaoJiShi/" 2>/dev/null || true

# Clean up pycache
find "${PACKAGE_DIR}/opt/DaoJiShi" -name "__pycache__" -type d -exec rm -rf {} +

# Copy launch script
cp uos_packaging/launch.sh "${PACKAGE_DIR}/opt/DaoJiShi/"
chmod +x "${PACKAGE_DIR}/opt/DaoJiShi/launch.sh"

# Control file
# Copy and update architecture to all (since it's python source)
cp uos_packaging/control "${PACKAGE_DIR}/DEBIAN/"
# sed -i "s/Architecture: .*/Architecture: all/" "${PACKAGE_DIR}/DEBIAN/control"

# Post-install script
cp uos_packaging/postinst "${PACKAGE_DIR}/DEBIAN/"
chmod 755 "${PACKAGE_DIR}/DEBIAN/postinst"

# Desktop file
cp uos_packaging/DaoJiShi.desktop "${PACKAGE_DIR}/usr/share/applications/"

# Icon Processing
echo "Processing icon..."
ICON_SRC=""
if [ -f "app/ui/favicon.ico" ]; then
    ICON_SRC="app/ui/favicon.ico"
elif [ -f "app/source/time.ico" ]; then
    ICON_SRC="app/source/time.ico"
fi

if [ -n "$ICON_SRC" ]; then
    # Convert ICO to PNG using our helper script
    # We use the python environment we are in
    echo "Converting $ICON_SRC to PNG..."
    python3 uos_packaging/convert_icon.py "$ICON_SRC" "${PACKAGE_DIR}/usr/share/icons/hicolor/256x256/apps/daojishi.png" 256
    
    # Check if conversion succeeded
    if [ ! -f "${PACKAGE_DIR}/usr/share/icons/hicolor/256x256/apps/daojishi.png" ]; then
        echo "Warning: Icon conversion failed. Fallback to direct copy (might not show up)."
        cp "$ICON_SRC" "${PACKAGE_DIR}/usr/share/icons/hicolor/256x256/apps/daojishi.png"
    fi
    
    # Copy to /opt/DaoJiShi for reference/backup (used by desktop file absolute path)
    cp "${PACKAGE_DIR}/usr/share/icons/hicolor/256x256/apps/daojishi.png" "${PACKAGE_DIR}/opt/DaoJiShi/daojishi.png"
else
    echo "Warning: No icon file found!"
fi

# 6. Build DEB
echo "[5/5] Building .deb package..."
# Calculate size (in KB)
SIZE=$(du -s "${PACKAGE_DIR}" | cut -f1)
# Add Installed-Size to control file
echo "Installed-Size: $SIZE" >> "${PACKAGE_DIR}/DEBIAN/control"

# Build
DEB_NAME="DaoJiShi_1.0.0_${ARCH}.deb"
dpkg-deb --build "${PACKAGE_DIR}" "${WORK_DIR}/${DEB_NAME}"

echo "=== Build Complete ==="
echo "Package saved to: ${WORK_DIR}/${DEB_NAME}"
echo "You can install it using: sudo dpkg -i ${DEB_NAME}"
