import os
from datetime import datetime
from core.config import BASE_DIR
from PIL import ImageGrab



def capture_screenshot():
    output_folder = f'{BASE_DIR}/store'
    os.makedirs(output_folder, exist_ok=True)

    screenshot = ImageGrab.grab()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(output_folder, filename)
    screenshot.save(filepath)
    print(f"Screenshot saved to {filepath}")
