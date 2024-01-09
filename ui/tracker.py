import logging
import sys
import threading
import random
import time

from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QRadioButton, QMessageBox
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtCore import QTimer, QTime, QSize, Qt
from PySide6.QtGui import QIcon

from ui.main_ui import Ui_MainWindow
from ui.dialog import ScreenshotDialog, message
from screenshot.main import capture_screenshot
from storage.database import Database
from storage.events import session_start, get_current_session, update_session, save_tracked_time
from events.mouse_events import MouseListener
from events.timer import Timer


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.radio_buttons = []
        self.session = None
        self.screenshot_process = None
        self.screenshot_time = 15
        self.dialog = ScreenshotDialog()
        self.status = False

        self.counted_time = 0
        self.project = None

        # Connection to db
        self.db = Database()

        # UI

        self.ui = Ui_MainWindow()
        self.timer_thread = Timer(self.ui)
        self.ui.setupUi(self)
        self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
        self.ui.control_btn.clicked.connect(self.play)
        self.render_projects()

        self.screenshot_timer = QTimer(self)
        self.screenshot_timer.timeout.connect(self.capture_screenshot_threaded)
        self.close_dialog_timer = QTimer(self)
        self.close_dialog_timer.timeout.connect(self.close_dialog)
        self.thread_mouse_event = None

    def __del__(self):
        self.update_track_time()
        self.close_session()
        self.db.close()

    def close_session(self):
        session = get_current_session(self.db.get_query(), self.project)
        update_session(self.db.get_query(), session.get('id'))

    def play(self):
        if self.project is not None:
            if self.status is False:
                self.ui.control_btn.setIcon(QIcon(u":/resources/icons/stop.svg"))
                self.status = True
                self.runner()

            else:
                self.ui.control_btn.setIcon(QIcon(u":/resources/icons/play.svg"))
                self.status = False
                self.cleaner()
        else:
            message('you should select a project')

        self.radio_button_switcher()

    def runner(self):
        session_start(self.db.get_query(), self.project)
        # self.screenshot_time = random.randint(180, 600)
        self.screenshot_timer.start(self.screenshot_time * 1000)
        self.close_dialog_timer.start((self.screenshot_time + 5) * 1000)
        self.timer_thread.run()
        self.thread_mouse_event = MouseListener(self.db.get_query(), get_current_session(
            self.db.get_query(), self.project).get('id'))
        self.thread_mouse_event.run()
        logging.info('Track is started...')

    def cleaner(self):
        self.screenshot_timer.stop()
        self.thread_mouse_event.stop_listener()
        self.update_track_time()
        logging.info('Track is stopped...')
        self.timer_thread.stop()

    def capture_screenshot_threaded(self):
        # self.screenshot_time = random.randint(180, 600)
        logging.info(f'Screenshot time: {self.screenshot_time}')
        query = self.db.get_query()
        screenshot_thread = threading.Thread(target=capture_screenshot,
                                             args=(query, get_current_session(query, self.project).get('id'),))
        screenshot_thread.start()
        self.update_screenshot_data(query)

    def load_image_from_url(self, url, formatted_datetime):
        pixmap = QPixmap(url)
        self.dialog.screenshot.setPixmap(pixmap)
        self.dialog.screenshot.setScaledContents(True)
        self.dialog.title.setText(formatted_datetime)
        self.dialog.show()
        print("Dialog is visible:", self.dialog.isVisible())

    def close_dialog(self):
        self.dialog.close()

    def update_screenshot_data(self, query):
        session = get_current_session(query, self.project)
        image_path = session.get('last_screenshot_path')
        if image_path:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
            self.load_image_from_url(image_path, formatted_datetime)

    def render_projects(self):
        for i in range(10):
            project = QRadioButton(self.ui.projects)
            project.setText(f"Project {i + 1}")
            project.setStyleSheet(u"QRadioButton{\n"
                                  "	padding: 10px;\n"
                                  "	background-color: rgb(204, 206, 219);\n"
                                  "	font-size: 16px;\n"
                                  "	color: #000;\n"
                                  "}\n"
                                  "")

            project.setObjectName(u"project")
            project.setMinimumSize(QSize(0, 40))
            project.setMaximumSize(QSize(16777215, 40))
            project.setCursor(QCursor(Qt.PointingHandCursor))
            project.clicked.connect(self.radio_button_clicked)
            self.ui.verticalLayout_2.addWidget(project)
            self.radio_buttons.append(project)

    def radio_button_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.project = sender.text()
            query = self.db.get_query()
            session = get_current_session(query, sender.text())

            if session.get('project') != self.project:
                self.timer_thread = Timer(self.ui)
                self.timer_thread.update_time()

    def radio_button_switcher(self):
        for btn in self.radio_buttons:
            if self.status:
                if btn.text() != self.project:
                    btn.setDisabled(True)
            else:
                btn.setDisabled(False)

    def update_track_time(self):
        query = self.db.get_query()
        session = get_current_session(query, self.project)
        save_tracked_time(query, session.get('id'), self.timer_thread.formatted_time)
