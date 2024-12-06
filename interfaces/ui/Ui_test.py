# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

from qfluentwidgets import PushButton

class Ui_Test(object):
    def setupUi(self, Test):
        if not Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(400, 300)
        self.gridLayout = QGridLayout(Test)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = PushButton(Test)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.retranslateUi(Test)

        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Test", u"\u5207\u6362\u4e3b\u9898", None))
    # retranslateUi

