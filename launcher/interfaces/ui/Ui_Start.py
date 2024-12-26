# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ..Widgets import ModelDisplayCard
from qfluentwidgets import (DisplayLabel, PrimaryPushButton, PushButton)

class Ui_Start(object):
    def setupUi(self, Start):
        if not Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(896, 583)
        self.verticalLayout = QVBoxLayout(Start)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pHeader = QFrame(Start)
        self.pHeader.setObjectName(u"pHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pHeader.sizePolicy().hasHeightForWidth())
        self.pHeader.setSizePolicy(sizePolicy)
        self.pHeader.setMinimumSize(QSize(800, 200))
        self.pHeader.setAutoFillBackground(False)
        self.pHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.pHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.pHeader)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerInfo = DisplayLabel(self.pHeader)
        self.headerInfo.setObjectName(u"headerInfo")

        self.verticalLayout_2.addWidget(self.headerInfo)


        self.verticalLayout.addWidget(self.pHeader)

        self.pMain = QHBoxLayout()
        self.pMain.setObjectName(u"pMain")
        self.pDisplay = QGridLayout()
        self.pDisplay.setObjectName(u"pDisplay")
        self.pFolders = QGridLayout()
        self.pFolders.setObjectName(u"pFolders")
        self.LLMFolder = PushButton(Start)
        self.LLMFolder.setObjectName(u"LLMFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LLMFolder.sizePolicy().hasHeightForWidth())
        self.LLMFolder.setSizePolicy(sizePolicy1)

        self.pFolders.addWidget(self.LLMFolder, 0, 1, 1, 1)

        self.personaFolder = PushButton(Start)
        self.personaFolder.setObjectName(u"personaFolder")
        sizePolicy1.setHeightForWidth(self.personaFolder.sizePolicy().hasHeightForWidth())
        self.personaFolder.setSizePolicy(sizePolicy1)

        self.pFolders.addWidget(self.personaFolder, 1, 1, 1, 1)

        self.ASRFolder = PushButton(Start)
        self.ASRFolder.setObjectName(u"ASRFolder")
        sizePolicy1.setHeightForWidth(self.ASRFolder.sizePolicy().hasHeightForWidth())
        self.ASRFolder.setSizePolicy(sizePolicy1)

        self.pFolders.addWidget(self.ASRFolder, 0, 0, 1, 1)

        self.TTSFolder = PushButton(Start)
        self.TTSFolder.setObjectName(u"TTSFolder")
        sizePolicy1.setHeightForWidth(self.TTSFolder.sizePolicy().hasHeightForWidth())
        self.TTSFolder.setSizePolicy(sizePolicy1)

        self.pFolders.addWidget(self.TTSFolder, 0, 2, 1, 1)


        self.pDisplay.addLayout(self.pFolders, 2, 0, 1, 1)

        self.mgVSpacerT2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.mgVSpacerT2, 0, 0, 1, 1)

        self.mgVSpacerB2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.mgVSpacerB2, 3, 0, 1, 1)

        self.pModels = QGridLayout()
        self.pModels.setObjectName(u"pModels")
        self.ASRCard = ModelDisplayCard(Start)
        self.ASRCard.setObjectName(u"ASRCard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ASRCard.sizePolicy().hasHeightForWidth())
        self.ASRCard.setSizePolicy(sizePolicy2)

        self.pModels.addWidget(self.ASRCard, 0, 0, 1, 1)

        self.LLMCard = ModelDisplayCard(Start)
        self.LLMCard.setObjectName(u"LLMCard")
        sizePolicy2.setHeightForWidth(self.LLMCard.sizePolicy().hasHeightForWidth())
        self.LLMCard.setSizePolicy(sizePolicy2)

        self.pModels.addWidget(self.LLMCard, 0, 1, 1, 1)

        self.TTSCard = ModelDisplayCard(Start)
        self.TTSCard.setObjectName(u"TTSCard")
        sizePolicy2.setHeightForWidth(self.TTSCard.sizePolicy().hasHeightForWidth())
        self.TTSCard.setSizePolicy(sizePolicy2)

        self.pModels.addWidget(self.TTSCard, 0, 2, 1, 1)


        self.pDisplay.addLayout(self.pModels, 1, 0, 1, 1)


        self.pMain.addLayout(self.pDisplay)

        self.mgHSpacerL = QSpacerItem(60, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.pMain.addItem(self.mgHSpacerL)

        self.pStart = QGridLayout()
        self.pStart.setObjectName(u"pStart")
        self.startButton = PrimaryPushButton(Start)
        self.startButton.setObjectName(u"startButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy3)
        self.startButton.setMinimumSize(QSize(0, 0))
        self.startButton.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.startButton.setFont(font)

        self.pStart.addWidget(self.startButton, 4, 0, 1, 1)

        self.pBoard = QFrame(Start)
        self.pBoard.setObjectName(u"pBoard")
        self.pBoard.setMinimumSize(QSize(0, 120))
        self.pBoard.setFrameShape(QFrame.Shape.StyledPanel)
        self.pBoard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pBoard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.broadcast = DisplayLabel(self.pBoard)
        self.broadcast.setObjectName(u"broadcast")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(8)
        self.broadcast.setFont(font1)
        self.broadcast.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.broadcast)


        self.pStart.addWidget(self.pBoard, 2, 0, 1, 1)

        self.mulitFunc = QGridLayout()
        self.mulitFunc.setObjectName(u"mulitFunc")
        self.bButton = PushButton(Start)
        self.bButton.setObjectName(u"bButton")

        self.mulitFunc.addWidget(self.bButton, 0, 0, 1, 1)

        self.aButton = PushButton(Start)
        self.aButton.setObjectName(u"aButton")

        self.mulitFunc.addWidget(self.aButton, 0, 1, 1, 1)


        self.pStart.addLayout(self.mulitFunc, 5, 0, 1, 1)

        self.mgVSpacerB = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pStart.addItem(self.mgVSpacerB, 7, 0, 1, 1)

        self.mgVSpacerT = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pStart.addItem(self.mgVSpacerT, 1, 0, 1, 1)


        self.pMain.addLayout(self.pStart)

        self.mgHSpacerR = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.pMain.addItem(self.mgHSpacerR)


        self.verticalLayout.addLayout(self.pMain)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"Form", None))
        self.headerInfo.setText(QCoreApplication.translate("Start", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; color:#f0f0f0;\">\u79bb\u771f\u542f\u52a8\u5668</span></p></body></html>", None))
        self.LLMFolder.setText(QCoreApplication.translate("Start", u"LLM \u6a21\u578b\u76ee\u5f55", None))
        self.personaFolder.setText(QCoreApplication.translate("Start", u"\u63d0\u793a\u8bcd\u76ee\u5f55", None))
        self.ASRFolder.setText(QCoreApplication.translate("Start", u"ASR \u6a21\u578b\u76ee\u5f55", None))
        self.TTSFolder.setText(QCoreApplication.translate("Start", u"TTS \u6a21\u578b\u76ee\u5f55", None))
        self.startButton.setText(QCoreApplication.translate("Start", u"\u4e00\u952e\u542f\u52a8\uff01", None))
        self.broadcast.setText(QCoreApplication.translate("Start", u"<html><head/><body><p><span style=\" font-weight:700;\">\u516c\u544a\uff1a</span></p><p>\u563f\u563f\u563f...</p></body></html>", None))
        self.bButton.setText(QCoreApplication.translate("Start", u"PushButton", None))
        self.aButton.setText(QCoreApplication.translate("Start", u"PushButton", None))
    # retranslateUi

