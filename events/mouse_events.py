import logging

from pynput import mouse
from storage.connection import Storage

def on_click(x, y, button, pressed):
    if pressed:
        store = Storage()
        store.connect()
        data = {
            'x': x,
            'y': y,
            'button': str(button),
        }
        store.add_mouse_event(data)
        store.db.close()
        logging.info('Event added to db')
    return None


def run_mouse_click_listener():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
