import sys
import os
from PyQt5.QtGui import QIcon, QPixmap

def convert_ico_to_png(ico_path, png_path, size=256):
    app = None
    try:
        from PyQt5.QtWidgets import QApplication
        # QIcon/QPixmap requires a QGuiApplication or QApplication instance
        app = QApplication(sys.argv)
    except:
        pass

    if not os.path.exists(ico_path):
        print(f"Error: Input file not found: {ico_path}")
        sys.exit(1)

    try:
        icon = QIcon(ico_path)
        if icon.isNull():
            print("Error: Failed to load icon.")
            sys.exit(1)
            
        # Get pixmap of desired size
        pixmap = icon.pixmap(size, size)
        if pixmap.isNull():
            print("Error: Failed to create pixmap from icon.")
            sys.exit(1)
            
        # Save as PNG
        if pixmap.save(png_path, "PNG"):
            print(f"Successfully converted {ico_path} to {png_path}")
            sys.exit(0)
        else:
            print("Error: Failed to save PNG file.")
            sys.exit(1)
    except Exception as e:
        print(f"Exception during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_icon.py <input.ico> <output.png> [size]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_size = int(sys.argv[3]) if len(sys.argv) > 3 else 256
    
    convert_ico_to_png(input_file, output_file, target_size)
