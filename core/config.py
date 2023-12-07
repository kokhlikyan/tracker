import os
from pathlib import Path

APP_NAME = 'Tracker'
APP_LOCAL_FOLDER = os.path.join(os.path.expanduser('~'), f'.{APP_NAME}')
BASE_DIR = Path(__file__).parent.parent

