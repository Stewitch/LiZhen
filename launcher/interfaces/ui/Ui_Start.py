# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from ..Widgets import ModelDisplayCard
from qfluentwidgets import (CaptionLabel, DisplayLabel, PrimaryPushButton, PushButton,
    ScrollArea, TextBrowser)

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
        self.horizontalLayout = QHBoxLayout(self.pHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hInfoHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hInfoHSpacer)

        self.headerInfo = DisplayLabel(self.pHeader)
        self.headerInfo.setObjectName(u"headerInfo")
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        self.headerInfo.setFont(font)

        self.horizontalLayout.addWidget(self.headerInfo)


        self.verticalLayout.addWidget(self.pHeader)

        self.pMain = QHBoxLayout()
        self.pMain.setObjectName(u"pMain")
        self.pDisplay = QGridLayout()
        self.pDisplay.setObjectName(u"pDisplay")
        self.tVSpacerT = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.tVSpacerT, 0, 0, 1, 1)

        self.tVSpacerB = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.tVSpacerB, 2, 0, 1, 1)

        self.pModels = QGridLayout()
        self.pModels.setObjectName(u"pModels")
        self.ASRCard = ModelDisplayCard(Start)
        self.ASRCard.setObjectName(u"ASRCard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ASRCard.sizePolicy().hasHeightForWidth())
        self.ASRCard.setSizePolicy(sizePolicy1)

        self.pModels.addWidget(self.ASRCard, 0, 0, 1, 1)

        self.TTSCard = ModelDisplayCard(Start)
        self.TTSCard.setObjectName(u"TTSCard")
        sizePolicy1.setHeightForWidth(self.TTSCard.sizePolicy().hasHeightForWidth())
        self.TTSCard.setSizePolicy(sizePolicy1)

        self.pModels.addWidget(self.TTSCard, 0, 2, 1, 1)

        self.LLMCard = ModelDisplayCard(Start)
        self.LLMCard.setObjectName(u"LLMCard")
        sizePolicy1.setHeightForWidth(self.LLMCard.sizePolicy().hasHeightForWidth())
        self.LLMCard.setSizePolicy(sizePolicy1)

        self.pModels.addWidget(self.LLMCard, 0, 1, 1, 1)


        self.pDisplay.addLayout(self.pModels, 7, 0, 1, 1)

        self.pFolders = ScrollArea(Start)
        self.pFolders.setObjectName(u"pFolders")
        self.pFolders.setWidgetResizable(True)
        self.pFolderWidgets = QWidget()
        self.pFolderWidgets.setObjectName(u"pFolderWidgets")
        self.pFolderWidgets.setGeometry(QRect(0, 0, 582, 200))
        sizePolicy.setHeightForWidth(self.pFolderWidgets.sizePolicy().hasHeightForWidth())
        self.pFolderWidgets.setSizePolicy(sizePolicy)
        self.pFolderWidgets.setMinimumSize(QSize(0, 200))
        self.gridLayout = QGridLayout(self.pFolderWidgets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LLMFolder = PushButton(self.pFolderWidgets)
        self.LLMFolder.setObjectName(u"LLMFolder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LLMFolder.sizePolicy().hasHeightForWidth())
        self.LLMFolder.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.LLMFolder.setFont(font1)

        self.gridLayout.addWidget(self.LLMFolder, 0, 1, 1, 1)

        self.ASRFolder = PushButton(self.pFolderWidgets)
        self.ASRFolder.setObjectName(u"ASRFolder")
        sizePolicy2.setHeightForWidth(self.ASRFolder.sizePolicy().hasHeightForWidth())
        self.ASRFolder.setSizePolicy(sizePolicy2)
        self.ASRFolder.setFont(font1)

        self.gridLayout.addWidget(self.ASRFolder, 0, 0, 1, 1)

        self.TTSFolder = PushButton(self.pFolderWidgets)
        self.TTSFolder.setObjectName(u"TTSFolder")
        sizePolicy2.setHeightForWidth(self.TTSFolder.sizePolicy().hasHeightForWidth())
        self.TTSFolder.setSizePolicy(sizePolicy2)
        self.TTSFolder.setFont(font1)

        self.gridLayout.addWidget(self.TTSFolder, 0, 2, 1, 1)

        self.personaFolder = PushButton(self.pFolderWidgets)
        self.personaFolder.setObjectName(u"personaFolder")
        sizePolicy2.setHeightForWidth(self.personaFolder.sizePolicy().hasHeightForWidth())
        self.personaFolder.setSizePolicy(sizePolicy2)
        self.personaFolder.setFont(font1)

        self.gridLayout.addWidget(self.personaFolder, 1, 0, 1, 1)

        self.pFolders.setWidget(self.pFolderWidgets)

        self.pDisplay.addWidget(self.pFolders, 9, 0, 1, 1)

        self.cFVSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.cFVSpacer, 8, 0, 1, 1)

        self.modelTitle = QHBoxLayout()
        self.modelTitle.setObjectName(u"modelTitle")
        self.tMGHSpacerL = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.modelTitle.addItem(self.tMGHSpacerL)

        self.mTitleLabel = DisplayLabel(Start)
        self.mTitleLabel.setObjectName(u"mTitleLabel")
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.mTitleLabel.setFont(font2)

        self.modelTitle.addWidget(self.mTitleLabel)


        self.pDisplay.addLayout(self.modelTitle, 1, 0, 1, 1)

        self.mgVSpacerB2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pDisplay.addItem(self.mgVSpacerB2, 10, 0, 1, 1)

        self.characterCard = QFrame(Start)
        self.characterCard.setObjectName(u"characterCard")
        self.characterCard.setMinimumSize(QSize(0, 50))
        self.characterCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.characterCard.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.characterCard)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.characterHeader = CaptionLabel(self.characterCard)
        self.characterHeader.setObjectName(u"characterHeader")
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font3.setPointSize(12)
        self.characterHeader.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.characterHeader)

        self.characterName = CaptionLabel(self.characterCard)
        self.characterName.setObjectName(u"characterName")
        self.characterName.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.characterName)

        self.agentHeader = CaptionLabel(self.characterCard)
        self.agentHeader.setObjectName(u"agentHeader")
        self.agentHeader.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.agentHeader)

        self.agentName = CaptionLabel(self.characterCard)
        self.agentName.setObjectName(u"agentName")
        self.agentName.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.agentName)

        self.l2dName = CaptionLabel(self.characterCard)
        self.l2dName.setObjectName(u"l2dName")
        self.l2dName.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.l2dName)

        self.l2dHeader = CaptionLabel(self.characterCard)
        self.l2dHeader.setObjectName(u"l2dHeader")
        self.l2dHeader.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.l2dHeader)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.pDisplay.addWidget(self.characterCard, 3, 0, 1, 1)


        self.pMain.addLayout(self.pDisplay)

        self.mgHSpacerL = QSpacerItem(60, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.pMain.addItem(self.mgHSpacerL)

        self.pStart = QGridLayout()
        self.pStart.setObjectName(u"pStart")
        self.mulitFunc = QGridLayout()
        self.mulitFunc.setObjectName(u"mulitFunc")
        self.toConsoleButton = PushButton(Start)
        self.toConsoleButton.setObjectName(u"toConsoleButton")
        font4 = QFont()
        font4.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.toConsoleButton.setFont(font4)

        self.mulitFunc.addWidget(self.toConsoleButton, 0, 0, 1, 1)

        self.toSettingButton = PushButton(Start)
        self.toSettingButton.setObjectName(u"toSettingButton")
        self.toSettingButton.setFont(font4)

        self.mulitFunc.addWidget(self.toSettingButton, 0, 1, 1, 1)


        self.pStart.addLayout(self.mulitFunc, 5, 0, 1, 1)

        self.bTitle = DisplayLabel(Start)
        self.bTitle.setObjectName(u"bTitle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bTitle.sizePolicy().hasHeightForWidth())
        self.bTitle.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.bTitle.setFont(font5)

        self.pStart.addWidget(self.bTitle, 1, 0, 1, 1)

        self.mgVSpacerB = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pStart.addItem(self.mgVSpacerB, 7, 0, 1, 1)

        self.broadcast = TextBrowser(Start)
        self.broadcast.setObjectName(u"broadcast")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.broadcast.sizePolicy().hasHeightForWidth())
        self.broadcast.setSizePolicy(sizePolicy4)
        self.broadcast.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font6.setPointSize(10)
        self.broadcast.setFont(font6)

        self.pStart.addWidget(self.broadcast, 2, 0, 1, 1)

        self.startButton = PrimaryPushButton(Start)
        self.startButton.setObjectName(u"startButton")
        sizePolicy2.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy2)
        self.startButton.setMinimumSize(QSize(0, 0))
        self.startButton.setMaximumSize(QSize(16777215, 80))
        font7 = QFont()
        font7.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font7.setPointSize(20)
        font7.setBold(True)
        self.startButton.setFont(font7)

        self.pStart.addWidget(self.startButton, 4, 0, 1, 1)

        self.bTMGVspacerT = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pStart.addItem(self.bTMGVspacerT, 0, 0, 1, 1)

        self.bSMGVSpacer = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.pStart.addItem(self.bSMGVSpacer, 3, 0, 1, 1)


        self.pMain.addLayout(self.pStart)

        self.mgHSpacerR = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.pMain.addItem(self.mgHSpacerR)


        self.verticalLayout.addLayout(self.pMain)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"Form", None))
        self.headerInfo.setText(QCoreApplication.translate("Start", u"<html><head/><body><p><span style=\" font-size:16pt; color:#dedede;\">Open-LLM-VTuber WebUI</span></p><p><span style=\" font-size:20pt; font-weight:700; color:#dedede;\">\u79bb\u771f \u542f\u52a8\u5668</span></p><p><span style=\" font-size:14pt; color:#dedede;\">\u538c\u5026\u4e86\u73b0\u5b9e\u7684\u4eba\u9645\u4ea4\u5f80\uff1f\u90a3\u5c31\u9003\u79bb\u73b0\u5b9e\u5427\uff01</span></p></body></html>", None))
        self.LLMFolder.setText(QCoreApplication.translate("Start", u"LLM \u6a21\u578b\u76ee\u5f55", None))
        self.ASRFolder.setText(QCoreApplication.translate("Start", u"ASR \u6a21\u578b\u76ee\u5f55", None))
        self.TTSFolder.setText(QCoreApplication.translate("Start", u"TTS \u6a21\u578b\u76ee\u5f55", None))
        self.personaFolder.setText(QCoreApplication.translate("Start", u"\u63d0\u793a\u8bcd\u76ee\u5f55", None))
        self.mTitleLabel.setText(QCoreApplication.translate("Start", u"\u89d2\u8272 & \u6a21\u578b\u533a", None))
        self.characterHeader.setText(QCoreApplication.translate("Start", u"\u89d2\u8272\uff1a", None))
        self.characterName.setText(QCoreApplication.translate("Start", u"None", None))
        self.agentHeader.setText(QCoreApplication.translate("Start", u"\u5bf9\u8bdd\u4ee3\u7406\uff1a", None))
        self.agentName.setText(QCoreApplication.translate("Start", u"None", None))
        self.l2dName.setText(QCoreApplication.translate("Start", u"None", None))
        self.l2dHeader.setText(QCoreApplication.translate("Start", u"Live2D\u6a21\u578b\uff1a", None))
        self.toConsoleButton.setText(QCoreApplication.translate("Start", u"\u63a7\u5236\u53f0", None))
        self.toSettingButton.setText(QCoreApplication.translate("Start", u"\u8bbe\u7f6e", None))
        self.bTitle.setText(QCoreApplication.translate("Start", u"\u516c\u544a", None))
        self.broadcast.setHtml(QCoreApplication.translate("Start", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u516c\u544a\u533a\u53ef\u6eda\u52a8\uff0c\u8bf7</span><span style=\" font-size:12pt; font-weight:700; color:#ff0000;\">\u5b8c\u5168\u9605\u8bfb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u4e3a <span style=\" fo"
                        "nt-weight:700;\">0.5.6</span> \u7248\u672c <span style=\" font-weight:700;\">\u53ef\u80fd\u5b58\u5728\u8f83\u591a\u95ee\u9898\uff0c\u8bf7\u53ca\u65f6\u53cd\u9988</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github\u94fe\u63a5\u53ef\u5728<span style=\" font-weight:700;\">\u8bbe\u7f6e</span>\u4e2d\u627e\u5230</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u76ee\u524d\u5e76<span style=\" font-weight:700; color:#ff0000;\">\u4e0d\u652f\u6301CUDA&amp;CUDNN&amp;FFMpeg\u81ea\u52a8\u914d\u7f6e</span>\uff0c\u5bf9\u4e8eN\u5361\u7528\u6237\uff0c\u8bf7\u524d\u5f80 <span style=\" font-weight:700; color:#ff0000;\">\u6587\u6863#Nvidia GPU \u652f\u6301</span> \u67e5\u770b\u6559\u7a0b</p></body></html>", None))
        self.startButton.setText(QCoreApplication.translate("Start", u"\u4e00\u952e\u542f\u52a8\uff01", None))
    # retranslateUi

