import time

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from .screenshot_dialog import Ui_Dialog


class ScreenshotDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ScreenshotDialog, self).__init__()
        self.setupUi(self)


def message(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec()
