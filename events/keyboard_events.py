import keyboard
from PySide6.QtCore import Signal, QThread


class KeyboardMonitorThread(QThread):
    key_pressed = Signal(str)

    def run(self):
        keyboard.hook(self.keyboard_event_handler)

    def keyboard_event_handler(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            self.key_pressed.emit(key)