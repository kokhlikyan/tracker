import threading
from pynput import keyboard


class KeyboardListenerThread(threading.Thread):
    def __init__(self):
        super(KeyboardListenerThread, self).__init__()

    def on_press(self, key):
        try:
            print(f'Key pressed: {key.char}')
        except AttributeError:
            print(f'Special key pressed: {key}')

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.start()
