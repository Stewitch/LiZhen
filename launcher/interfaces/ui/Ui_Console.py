# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Console.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import (CommandBar, DisplayLabel, TextBrowser)

class Ui_Console(object):
    def setupUi(self, Console):
        if not Console.objectName():
            Console.setObjectName(u"Console")
        Console.resize(943, 597)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Console.sizePolicy().hasHeightForWidth())
        Console.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Console)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Header = QHBoxLayout()
        self.Header.setObjectName(u"Header")
        self.hHSpacerL = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.Header.addItem(self.hHSpacerL)

        self.title = DisplayLabel(Console)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)

        self.Header.addWidget(self.title)

        self.shellName = DisplayLabel(Console)
        self.shellName.setObjectName(u"shellName")
        sizePolicy1.setHeightForWidth(self.shellName.sizePolicy().hasHeightForWidth())
        self.shellName.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Alibaba PuHuiTi R"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.shellName.setFont(font1)

        self.Header.addWidget(self.shellName)

        self.status = DisplayLabel(Console)
        self.status.setObjectName(u"status")
        sizePolicy1.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy1)
        self.status.setFont(font1)

        self.Header.addWidget(self.status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Header.addItem(self.horizontalSpacer)

        self.cBContainer = QWidget(Console)
        self.cBContainer.setObjectName(u"cBContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cBContainer.sizePolicy().hasHeightForWidth())
        self.cBContainer.setSizePolicy(sizePolicy2)
        self.cBContainer.setMinimumSize(QSize(375, 0))
        self.cBContainer.setMaximumSize(QSize(375, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.cBContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cmdBar = CommandBar(self.cBContainer)
        self.cmdBar.setObjectName(u"cmdBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cmdBar.sizePolicy().hasHeightForWidth())
        self.cmdBar.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Alibaba PuHuiTi R"])
        font2.setPointSize(10)
        self.cmdBar.setFont(font2)

        self.horizontalLayout_4.addWidget(self.cmdBar)


        self.Header.addWidget(self.cBContainer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.Header.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.Header)

        self.Shells = QStackedWidget(Console)
        self.Shells.setObjectName(u"Shells")
        self.PShell = QWidget()
        self.PShell.setObjectName(u"PShell")
        self.horizontalLayout_2 = QHBoxLayout(self.PShell)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.projectShell = TextBrowser(self.PShell)
        self.projectShell.setObjectName(u"projectShell")
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font3.setPointSize(10)
        self.projectShell.setFont(font3)

        self.horizontalLayout_2.addWidget(self.projectShell)

        self.Shells.addWidget(self.PShell)
        self.LShell = QWidget()
        self.LShell.setObjectName(u"LShell")
        self.horizontalLayout_3 = QHBoxLayout(self.LShell)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.launcherShell = TextBrowser(self.LShell)
        self.launcherShell.setObjectName(u"launcherShell")

        self.horizontalLayout_3.addWidget(self.launcherShell)

        self.Shells.addWidget(self.LShell)

        self.verticalLayout.addWidget(self.Shells)


        self.retranslateUi(Console)

        QMetaObject.connectSlotsByName(Console)
    # setupUi

    def retranslateUi(self, Console):
        Console.setWindowTitle(QCoreApplication.translate("Console", u"Form", None))
        self.title.setText(QCoreApplication.translate("Console", u"\u63a7\u5236\u53f0\uff1a", None))
        self.shellName.setText(QCoreApplication.translate("Console", u"ShellName", None))
        self.status.setText(QCoreApplication.translate("Console", u"Status", None))
    # retranslateUi

