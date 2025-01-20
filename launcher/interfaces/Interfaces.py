from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from qfluentwidgets import (ScrollArea, ExpandLayout, PrimaryPushButton, FluentIcon,
                            InfoBar)

from ..utils.enums import StyleSheet
from ..utils.log import logger

import random



class ManagerInterface(ScrollArea):
    def __init__(self, parent=None, title:str = "管理", enableSave: bool = False):
        super().__init__(parent=parent)
        self.view = QWidget()
        self.expandLayout = ExpandLayout(self.view)
        self.enableSave = enableSave
        
        self.titleLabel = QLabel(self.tr(title), self)
        
        self._init()
        
        logger.info(f"{title} 界面初始化，对象名称：{self.objectName()}")
    
      
    def _setGroups(self):
        """在此声明卡片组"""
        pass
    
    
    def _setCards(self):
        """在此声明卡片"""
        pass
    
    
    def _addCards2Groups(self):
        """在此将卡片添加到对应卡片组"""
        pass
    
    
    def _addGroups2Layout(self):
        """在此将卡片组添加到布局"""
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
    
    
    def _Layout(self):
        self.titleLabel.move(36, 30)
        self._addGroups2Layout()

    
    def _SSConnection(self):
        """在此连接信号与槽"""
        pass
    
    
    def _init(self):
        self._setGroups()
        self._setCards()
        self._addCards2Groups()
        
        self.resize(1000,800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName(f"ManagerInterface_{str(random.randint(100000, 999999))}")
        self.view.setObjectName('View')
        self.titleLabel.setObjectName('TitleLabel')
        
        StyleSheet.MANAGER.apply(self)
        
        if self.enableSave:
            self._enableSaveButton()
        
        self._Layout()
        self._SSConnection()
    
    
    def _enableSaveButton(self):
        """启用保存按钮"""
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(10)
        self.saveButton = PrimaryPushButton(FluentIcon.SAVE, self.tr("保存"), self)
        self.saveButton.setFont(font)
        self.saveButton.setEnabled(False)
        self.setViewportMargins(0, 80, 0, 52)
        self.saveButton.move(810, 608)
        
        
    def resizeEvent(self, e):
        if self.enableSave:
            mgx, mgy = 125, -88
            self.saveButton.move(e.size().width()-mgx, e.size().height()-mgy)
        return super().resizeEvent(e)
    
    def _showErrorBar(self, msg):
        InfoBar.error(
            self.tr("错误"),
            msg,
            duration=1500,
            parent=self
        )
    
    def _showWarnBar(self, msg):
        InfoBar.warning(
            self.tr("警告"),
            msg,
            duration=1500,
            parent=self
        )
    
    def _showInfoBar(self, msg):
        InfoBar.info(
            self.tr("信息"),
            msg,
            duration=1500,
            parent=self
        )