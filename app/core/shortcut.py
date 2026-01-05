import platform
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

# Check if keyboard is available and usable (requires root on Linux usually)
try:
    import keyboard
    HAS_KEYBOARD = True
except ImportError:
    HAS_KEYBOARD = False

class ShortcutManager(QObject):
    triggered = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.hotkeys = {} # For keyboard lib
        self.qshortcuts = {} # For PyQt shortcuts
        self.window = None
        self.use_native = False
        
        # On Linux, default to native Qt shortcuts to avoid root requirement
        if platform.system() == "Linux":
            self.use_native = True

    def set_window(self, window):
        """Set the main window for context-aware shortcuts (Qt)"""
        self.window = window

    def register(self, action_name, key_sequence):
        if not key_sequence:
            return

        # Clear existing
        self._unregister(action_name)

        if self.use_native and self.window:
            self._register_qt(action_name, key_sequence)
        elif HAS_KEYBOARD:
            try:
                self._register_keyboard(action_name, key_sequence)
            except Exception as e:
                print(f"Global hotkey failed for {action_name}: {e}. Falling back to Qt.")
                if self.window:
                    self._register_qt(action_name, key_sequence)
        elif self.window:
            self._register_qt(action_name, key_sequence)

    def _register_keyboard(self, action_name, key_sequence):
        # Lambda to emit signal
        callback = lambda: self.triggered.emit(action_name)
        # Store the remover function or handle
        self.hotkeys[action_name] = keyboard.add_hotkey(key_sequence, callback)

    def _register_qt(self, action_name, key_sequence):
        # Convert simple key strings if needed, though Qt handles most like "ctrl+m"
        shortcut = QShortcut(QKeySequence(key_sequence), self.window)
        # We use a closure to capture action_name
        shortcut.activated.connect(lambda a=action_name: self.triggered.emit(a))
        self.qshortcuts[action_name] = shortcut

    def _unregister(self, action_name):
        # Remove from keyboard lib
        if action_name in self.hotkeys:
            try:
                keyboard.remove_hotkey(self.hotkeys[action_name])
            except:
                pass
            del self.hotkeys[action_name]
            
        # Remove from Qt
        if action_name in self.qshortcuts:
            self.qshortcuts[action_name].setEnabled(False)
            self.qshortcuts[action_name].setParent(None)
            del self.qshortcuts[action_name]

    def clear(self):
        if HAS_KEYBOARD:
            try:
                keyboard.unhook_all()
            except:
                pass
        self.hotkeys = {}
        
        for s in self.qshortcuts.values():
            s.setEnabled(False)
            s.setParent(None)
        self.qshortcuts = {}
