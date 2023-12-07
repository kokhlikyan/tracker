import multiprocessing
from PySide6.QtWidgets import QMainWindow
from ui.main_ui import Ui_MainWindow
from PySide6.QtCore import QTimer, QTime
from PySide6.QtGui import QIcon
from screenshot.main import capture_screenshot


class ExpenseTracker(QMainWindow):
    def __init__(self):
        self.status = False
        self.elapsed_time = QTime(0, 0)
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
        self.ui.control_btn.clicked.connect(self.play)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.screenshot_timer = QTimer(self)
        self.screenshot_timer.timeout.connect(self.start_tracking)

    def play(self):
        if self.status is False:
            self.status = True
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/stop.svg"))
            self.timer.start(1000)
            self.screenshot_timer.start(5000)
        else:
            self.status = False
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
            self.timer.stop()
            self.screenshot_timer.stop()

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        formatted_time = self.elapsed_time.toString("hh:mm:ss")
        self.ui.timer_window.setText(formatted_time)

    def start_tracking(self):
        self.screenshot_process = multiprocessing.Process(target=capture_screenshot)
        self.screenshot_process.start()
