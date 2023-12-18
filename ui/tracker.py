import random
import logging
import threading
from PySide6.QtWidgets import QMainWindow
from ui.main_ui import Ui_MainWindow
from PySide6.QtCore import QTimer, QTime
from PySide6.QtGui import QIcon
from screenshot.main import capture_screenshot
from events.mouse_events import run_mouse_click_listener

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.screenshot_process = None
        self.screenshot_time = 0
        self.status = False
        self.elapsed_time = QTime(0, 0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
        self.ui.control_btn.clicked.connect(self.play)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.screenshot_timer = QTimer(self)
        self.screenshot_timer.timeout.connect(self.capture_screenshot_threaded)



    def play(self):
        if self.status is False:
            self.screenshot_time = random.randint(180, 600)
            self.status = True
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/stop.svg"))
            self.timer.start(1000)
            self.screenshot_timer.start(self.screenshot_time * 1000)
            thr = threading.Thread(target=run_mouse_click_listener)
            thr.start()
            logging.info('Track is started...')
            logging.info(f'The next screenshot will be in: {round(self.screenshot_time / 60, 1)}m')
        else:
            self.status = False
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
            self.timer.stop()
            self.screenshot_timer.stop()
            logging.info('Track is stopped...')

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        formatted_time = self.elapsed_time.toString("hh:mm:ss")
        self.ui.timer_window.setText(formatted_time)

    def capture_screenshot_threaded(self):
        self.screenshot_time = random.randint(180, 600)
        logging.info(f'Screenshot time: {self.screenshot_time}')
        screenshot_thread = threading.Thread(target=capture_screenshot)
        screenshot_thread.start()

