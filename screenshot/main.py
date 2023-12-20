import os
import logging
from datetime import datetime
from core.config import APP_LOCAL_FOLDER
from PIL import ImageGrab
from storage.events import set_last_screenshot_path

def capture_screenshot(query, session_id):
    try:
        folder_name = 'screenshot'
        os.makedirs(os.path.join(APP_LOCAL_FOLDER, folder_name), exist_ok=True)
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(APP_LOCAL_FOLDER, folder_name, filename)
        screenshot.save(filepath)
        set_last_screenshot_path(query,session_id, filepath)
        logging.info('Take screenshot...')


    except Exception as e:
        logging.error(f'Error: {e}')


