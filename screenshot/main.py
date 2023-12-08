import os
import logging
import asyncio
from datetime import datetime
from core.config import APP_LOCAL_FOLDER
from PIL import ImageGrab


def capture_screenshot():
    try:
        folder_name = 'screenshot'
        os.makedirs(os.path.join(APP_LOCAL_FOLDER, folder_name), exist_ok=True)
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(APP_LOCAL_FOLDER, folder_name, filename)
        screenshot.save(filepath)
        logging.info('Take screenshot...')
    except Exception as e:
        logging.error(f'Error: {e}')


