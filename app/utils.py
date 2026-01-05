import sys
import os

def get_resource_path(relative_path):
    """
    Get absolute path to resource.
    Compatible with Dev, PyInstaller --onefile, and --onedir.
    """
    # PyInstaller --onefile temp dir
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    
    # PyInstaller --onedir
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
        frozen_path = os.path.join(base_path, relative_path)
        if os.path.exists(frozen_path):
            return frozen_path
            
    # Development mode (or if not found in frozen path)
    # We look relative to the script location or current working directory
    # If running from source, relative_path like "app/source/..." assumes CWD is project root
    local_path = os.path.join(os.path.abspath("."), relative_path)
    if os.path.exists(local_path):
        return local_path
        
    return local_path
