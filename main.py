import os
import sys
import logging
from pathlib import Path
from PySide6.QtWidgets import QApplication
from ui.tracker import ExpenseTracker
from PySide6.QtCore import QDir
from core.config import APP_LOCAL_FOLDER
from storage.connection import Storage


def main():
    window = ExpenseTracker()
    window.show()
    return window


if __name__ == '__main__':
    try:
        os.makedirs(APP_LOCAL_FOLDER, exist_ok=True)
        log_file_path = os.path.join(APP_LOCAL_FOLDER, 'app.log')
        logging.basicConfig(level=logging.DEBUG, filename=log_file_path, filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('loging file is created...')
        os.chdir(Path.home())
        os.chdir(QDir.homePath())
        app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        os.environ["PATH"] += os.pathsep + app_path  # for Windows
        os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = app_path  # for macOS
        os.environ["LD_LIBRARY_PATH"] = app_path  # for Linux

        app = QApplication(sys.argv)
        w = main()
        sys.exit(app.exec())
    except Exception as e:
        logging.error(f'Error: {e}')
