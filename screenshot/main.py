import asyncio
import pyscreenshot as ImageGrab
from datetime import datetime
import schedule


async def take_screenshot():
    image_name = f'store/screenshot-{str(datetime.now())}'
    scr = ImageGrab.grab()
    filepath = f'{image_name}.png'

    await scr.save(filepath)

    return filepath
