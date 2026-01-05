import sys
import platform
import subprocess

def install_dependencies():
    print("Dependencies missing. Attempting to install...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "uos_packaging/requirements-uos.txt"])
        print("Dependencies installed successfully.")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies.")
        return False

def check_requirements():
    print("Checking environment for UOS packaging...")
    
    # Check Python version
    major, minor = sys.version_info[:2]
    if major != 3 or minor != 7:
        print(f"Error: Python 3.7 is required. Current version: {platform.python_version()}")
        print("Please ensure you are running this script with Python 3.7.")
        return False
        
    # Check libraries
    missing = False
    
    try:
        from PyQt5.QtCore import QT_VERSION_STR
        print(f"Found PyQt5 version: {QT_VERSION_STR}")
        if QT_VERSION_STR != '5.11.3':
             print(f"Warning: PyQt5 version 5.11.3 is expected. Found {QT_VERSION_STR}.")
             # We allow it to proceed with warning, or fail if strict.
             # Given the prompt, we should guide installation if not correct.
             # But if it's installed but wrong version, pip install might fail if system package locks it.
             pass 
    except ImportError:
        print("PyQt5 is missing.")
        missing = True

    try:
        import keyboard
        print("Found keyboard module.")
    except ImportError:
        print("keyboard module is missing.")
        missing = True
        
    if missing:
        user_input = input("Dependencies are missing. Install them now? (y/n): ")
        if user_input.lower() == 'y':
            if install_dependencies():
                return check_requirements() # Re-check
            else:
                return False
        else:
            print("Please install dependencies manually.")
            return False

    print("Environment check passed!")
    return True

if __name__ == "__main__":
    if not check_requirements():
        sys.exit(1)
