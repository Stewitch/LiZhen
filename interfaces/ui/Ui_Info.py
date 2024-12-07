# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Info.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (DisplayLabel, SmoothScrollArea)

class Ui_Info(object):
    def setupUi(self, Info):
        if not Info.objectName():
            Info.setObjectName(u"Info")
        Info.resize(789, 414)
        self.verticalLayout = QVBoxLayout(Info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = SmoothScrollArea(Info)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.view.setGeometry(QRect(0, 0, 757, 1900))
        self.view.setMinimumSize(QSize(0, 1900))
        self.label = DisplayLabel(self.view)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 85, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.ico_info = DisplayLabel(self.view)
        self.ico_info.setObjectName(u"ico_info")
        self.ico_info.setGeometry(QRect(10, 10, 31, 31))
        self.ico_info.setFont(font)
        self.scrollArea.setWidget(self.view)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Info)

        QMetaObject.connectSlotsByName(Info)
    # setupUi

    def retranslateUi(self, Info):
        Info.setWindowTitle(QCoreApplication.translate("Info", u"Form", None))
        self.label.setText(QCoreApplication.translate("Info", u"TextLabel", None))
        self.ico_info.setText(QCoreApplication.translate("Info", u"Icon", None))
    # retranslateUi

