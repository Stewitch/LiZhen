from qfluentwidgets import ScrollArea, ExpandLayout
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt

from ..utils.styles import StyleSheet


class SubInterface:
    pass



class ManagerInterface(ScrollArea):
    def __init__(self, parent=None, title:str = "管理"):
        super().__init__(parent=parent)
        self.view = QWidget()
        self.expandLayout = ExpandLayout(self.view)
        
        self.titleLabel = QLabel(self.tr(title), self)
        
        self._init()
    
      
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
        self.setObjectName('ManagerInterface')
        self.view.setObjectName('View')
        self.titleLabel.setObjectName('TitleLabel')
        
        StyleSheet.MANAGER.apply(self)
        
        self._Layout()
        self._SSConnection()