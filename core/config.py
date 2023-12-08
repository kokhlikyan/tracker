import logging
import os
import sys
from pathlib import Path

APP_NAME = 'Tracker'
APP_LOCAL_FOLDER = os.path.join(os.path.expanduser('~'), f'.{APP_NAME}')
BASE_DIR = Path(__file__).parent.parent


def create_folder(OUTPUT_FOLDER):
    try:
        executable_location = os.path.dirname(sys.executable)

        # Use the executable location as the current working directory
        os.chdir(executable_location)
        # Create the parent directory if it doesn't exist
        os.makedirs(APP_LOCAL_FOLDER, exist_ok=True)

        # Create the target directory
        output_folder = os.path.join(APP_LOCAL_FOLDER, OUTPUT_FOLDER)
        os.makedirs(output_folder, exist_ok=True)
        logging.info(f"Folder created successfully: {output_folder}")

    except Exception as e:
        # Log any exceptions
        logging.error(f"Error creating folder: {e}")
    return output_folder
