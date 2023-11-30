from PySide6.QtWidgets import QMainWindow
from ui.main_ui import Ui_MainWindow
from PySide6.QtCore import QTimer, QTime
from PySide6.QtGui import QIcon


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
        self.timer_screen = QTimer(self)
        self.timer.timeout.connect(self.update_time)

    def play(self):
        if self.status is False:
            self.status = True
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/stop.svg"))
            self.timer.start(1000)
        else:
            self.status = False
            self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
            self.timer.stop()

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        formatted_time = self.elapsed_time.toString("hh:mm:ss")
        self.ui.timer_window.setText(formatted_time)

