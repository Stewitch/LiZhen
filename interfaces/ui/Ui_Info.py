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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QWidget)

from qfluentwidgets import (DisplayLabel, HyperlinkButton, ImageLabel)

class Ui_Info(object):
    def setupUi(self, Info):
        if not Info.objectName():
            Info.setObjectName(u"Info")
        Info.resize(609, 428)
        Info.setMaximumSize(QSize(10000, 10000))
        self.gridLayout = QGridLayout(Info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.infoHeaderImg = ImageLabel(Info)
        self.infoHeaderImg.setObjectName(u"infoHeaderImg")

        self.gridLayout.addWidget(self.infoHeaderImg, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 8, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.authorInfo = DisplayLabel(Info)
        self.authorInfo.setObjectName(u"authorInfo")
        font = QFont()
        font.setFamilies([u"Britannic"])
        font.setPointSize(14)
        font.setBold(True)
        self.authorInfo.setFont(font)
        self.authorInfo.setTextFormat(Qt.TextFormat.AutoText)
        self.authorInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.authorInfo, 3, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.toGithub = HyperlinkButton(Info)
        self.toGithub.setObjectName(u"toGithub")

        self.gridLayout.addWidget(self.toGithub, 8, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)


        self.retranslateUi(Info)

        QMetaObject.connectSlotsByName(Info)
    # setupUi

    def retranslateUi(self, Info):
        Info.setWindowTitle(QCoreApplication.translate("Info", u"Form", None))
        self.infoHeaderImg.setText(QCoreApplication.translate("Info", u"infoHeaderImg", None))
        self.authorInfo.setText(QCoreApplication.translate("Info", u"<html><head/><body><p>\u57fa\u4e8e QFluentWidget \u5f00\u53d1\u7684 Open-LLM-VTuber \u542f\u52a8\u5668</p><p>By SunKSugaR.</p></body></html>", None))
        self.toGithub.setText(QCoreApplication.translate("Info", u"Github Repo", None))
    # retranslateUi

