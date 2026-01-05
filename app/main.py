import sys
import os
import logging
import traceback
from datetime import datetime

# Configure logging
def setup_logging():
    try:
        home = os.path.expanduser("~")
        log_dir = os.path.join(home, ".cache", "DaoJiShi")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        log_file = os.path.join(log_dir, "app.log")
        
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filemode='a'
        )
        
        # Also log to stdout for debugging
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.getLogger('').addHandler(console)
        
        logging.info("Application starting...")
        logging.info(f"Python version: {sys.version}")
        logging.info(f"Platform: {sys.platform}")
        
    except Exception as e:
        print(f"Failed to setup logging: {e}")

# Global exception handler
def exception_hook(exctype, value, tb):
    logging.critical("Uncaught exception:", exc_info=(exctype, value, tb))
    sys.__excepthook__(exctype, value, tb)

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtWidgets import QApplication

def main():
    setup_logging()
    sys.excepthook = exception_hook
    
    try:
        app = QApplication(sys.argv)
        app.setApplicationName("DaoJiShi")
        
        logging.info("Initializing MainWindow...")
        # Lazy import to ensure logging is set up before any potential import errors (e.g. missing DLLs)
        from app.ui.main_window import MainWindow
        
        window = MainWindow()
        window.show()
        
        logging.info("Entering event loop...")
        exit_code = app.exec_()
        
        logging.info(f"Application exited with code {exit_code}")
        sys.exit(exit_code)
        
    except Exception as e:
        logging.critical("Critical error in main loop:", exc_info=True)
        # Also print to stderr in case logging failed completely
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
