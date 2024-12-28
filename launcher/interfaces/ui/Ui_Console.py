# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Console.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import (CommandBar, DisplayLabel, TextBrowser)

class Ui_Console(object):
    def setupUi(self, Console):
        if not Console.objectName():
            Console.setObjectName(u"Console")
        Console.resize(943, 597)
        self.verticalLayout = QVBoxLayout(Console)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Header = QHBoxLayout()
        self.Header.setObjectName(u"Header")
        self.hHSpacerL = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.Header.addItem(self.hHSpacerL)

        self.title = DisplayLabel(Console)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)

        self.Header.addWidget(self.title)

        self.shellName = DisplayLabel(Console)
        self.shellName.setObjectName(u"shellName")
        sizePolicy.setHeightForWidth(self.shellName.sizePolicy().hasHeightForWidth())
        self.shellName.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Alibaba PuHuiTi R"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.shellName.setFont(font1)

        self.Header.addWidget(self.shellName)

        self.status = DisplayLabel(Console)
        self.status.setObjectName(u"status")
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setFont(font1)

        self.Header.addWidget(self.status)

        self.horizontalSpacer = QSpacerItem(440, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.Header.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cmdBar = CommandBar(Console)
        self.cmdBar.setObjectName(u"cmdBar")

        self.horizontalLayout.addWidget(self.cmdBar)


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
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font2.setPointSize(10)
        self.projectShell.setFont(font2)

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

