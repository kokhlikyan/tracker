# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import ui.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 619)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"QRadioButton{\n"
"	padding: 10px;\n"
"	background-color: rgb(204, 206, 219);\n"
"	font-size: 16px;\n"
"	color: #000;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_layout = QVBoxLayout(self.main_frame)
        self.main_layout.setSpacing(12)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(1, 1, -1, -1)
        self.timer_frame = QFrame(self.main_frame)
        self.timer_frame.setObjectName(u"timer_frame")
        self.timer_frame.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.timer_frame.setFrameShape(QFrame.StyledPanel)
        self.timer_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.timer_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.timer_window = QLabel(self.timer_frame)
        self.timer_window.setObjectName(u"timer_window")
        self.timer_window.setMinimumSize(QSize(200, 74))
        self.timer_window.setMaximumSize(QSize(200, 74))
        self.timer_window.setStyleSheet(u"background-color: rgb(237, 237, 237);\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.timer_window.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.timer_window, 0, 0, 1, 1)


        self.main_layout.addWidget(self.timer_frame)

        self.control_frame = QFrame(self.main_frame)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.control_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.control_btn = QPushButton(self.control_frame)
        self.control_btn.setObjectName(u"control_btn")
        self.control_btn.setMinimumSize(QSize(80, 80))
        self.control_btn.setMaximumSize(QSize(80, 80))
        self.control_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.control_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.control_btn.setIcon(icon)
        self.control_btn.setIconSize(QSize(80, 80))

        self.gridLayout_2.addWidget(self.control_btn, 0, 0, 1, 1)


        self.main_layout.addWidget(self.control_frame)

        self.content = QFrame(self.main_frame)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgba(0, 0, 0, 10);\n"
"border: none;\n"
"border-radius: 10px;")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.projects_title = QLabel(self.content)
        self.projects_title.setObjectName(u"projects_title")
        self.projects_title.setStyleSheet(u"padding: 10px;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color: #000;")

        self.verticalLayout.addWidget(self.projects_title)

        self.scrollArea = QScrollArea(self.content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 300))
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.projects = QWidget()
        self.projects.setObjectName(u"projects")
        self.projects.setGeometry(QRect(0, 0, 443, 330))
        self.verticalLayout_2 = QVBoxLayout(self.projects)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.projects)

        self.verticalLayout.addWidget(self.scrollArea)


        self.main_layout.addWidget(self.content)

        self.main_layout.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.timer_window.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.control_btn.setText("")
        self.projects_title.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
    # retranslateUi

