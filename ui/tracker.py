import random
import logging
import threading
import time

from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, QTime, QSize
from PySide6.QtGui import QIcon

from ui.main_ui import Ui_MainWindow
from screenshot.main import capture_screenshot
from storage.database import Database
from storage.events import session_start, get_current_session
from events.mouse_events import MouseListener


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.session = None
        self.screenshot_process = None
        self.screenshot_time = 0
        self.status = False

        # Connection to db
        self.db = Database()
        self.current_session = get_current_session(self.db.get_query())
        self.elapsed_time = QTime(0, 0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
        self.ui.control_btn.clicked.connect(self.play)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.screenshot_timer = QTimer(self)
        self.screenshot_timer.timeout.connect(self.capture_screenshot_threaded)

        self.thread_mouse_event = MouseListener(self.db.get_query(), get_current_session(self.db.get_query()).get('id'))

    def load_image_from_url(self, url):
        # Use QPixmap to load the image from the URL
        pixmap = QPixmap(url)
        # Set the pixmap to the QLabel
        self.ui.last_screenshot.setPixmap(pixmap)
        self.ui.last_screenshot.setScaledContents(True)
    def play(self):
        if self.status is False:
            self.screenshot_time = random.randint(180, 600)
            self.status = True
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/stop.svg"))
            self.timer.start(1000)
            self.screenshot_timer.start(self.screenshot_time * 1000)
            session_start(self.db.get_query())
            self.thread_mouse_event.run()
            logging.info('Track is started...')
            logging.info(f'The next screenshot will be in: {round(self.screenshot_time / 60, 1)}m')
        else:
            self.status = False
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
            self.timer.stop()
            self.screenshot_timer.stop()
            self.thread_mouse_event.stop_listener()

            logging.info('Track is stopped...')

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        formatted_time = self.elapsed_time.toString("hh:mm:ss")
        self.ui.timer_window.setText(formatted_time)

    def capture_screenshot_threaded(self):
        self.screenshot_time = random.randint(180, 600)
        logging.info(f'Screenshot time: {self.screenshot_time}')
        query = self.db.get_query()
        session = get_current_session(query)
        screenshot_thread = threading.Thread(target=capture_screenshot, args=(query, session.get('id'),))
        screenshot_thread.start()
        session = get_current_session(query)
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
        time.sleep(2)
        self.ui.last_screenshot_title.setText(f'Last screenshot: {formatted_datetime}')
        self.load_image_from_url(session.get('last_screenshot_path'))
