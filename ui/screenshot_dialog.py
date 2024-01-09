# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenshot_dialog.ui'
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
                           QPalette, QPixmap, QRadialGradient, QTransform, QGuiApplication)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_Dialog(object):

    def __init__(self):
        super(Ui_Dialog, self).__init__()

    def set_position(self, right, bottom):
        # Get the available screen geometry
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Calculate the new position
        new_x = screen_geometry.width() - (self.width() - 220)
        new_y = screen_geometry.height() - (self.height() / 2)

        # Set the new position
        self.setGeometry(new_x, new_y, self.width(), self.height())

    def setupUi(self, Dialog):
        self.set_position(right=0, bottom=0)
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))
        self.title.setMaximumSize(QSize(16777215, 30))
        self.title.setStyleSheet(u"color: #000;\n"
                                 "border-bottom: 1px solid silver;\n"
                                 "font-size: 16px;")

        self.verticalLayout.addWidget(self.title)

        self.screenshot = QLabel(Dialog)
        self.screenshot.setObjectName(u"screenshot")

        self.verticalLayout.addWidget(self.screenshot)


        QMetaObject.connectSlotsByName(Dialog)



    # setupUi


