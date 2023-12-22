import logging
import threading
from pynput import mouse
from storage.events import add_or_update_mouse_event


class MouseListener(threading.Thread):
    def __init__(self, query, session_id):
        super(MouseListener, self).__init__()
        self.query = query
        self.session_id = session_id
        self.daemon = True
        self.listener = None
        self.running = False

    def on_click(self, x, y, button, pressed):
        if pressed:
            left, right = 0, 0
            if button._name_ == 'left':
                left = 1
            elif button._name_ == 'right':
                right = 1
            add_or_update_mouse_event(self.query, self.session_id, left, right)

    def run(self):
        if not self.running:
            self.listener = mouse.Listener(on_click=self.on_click)
            self.listener.start()
            self.running = True
            logging.info('mouse event listener is started')

    def stop_listener(self):
        if self.running:
            self.listener.stop()
            self.listener.join()
            self.running = False
            logging.info('mouse event listener is stoped')
