class SubInterface:
    pass

from qfluentwidgets import *
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt
from utils.config import cfg
from utils.style import StyleSheet

class SettingInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.view = QWidget()
        self.expandLayout = ExpandLayout(self.view)

        self.label = DisplayLabel(self.tr("设置"), self)
        self.label.setObjectName('settingLabel')
    
        self.__initInterface()
        self.__initLayout()
        self.__connectSignals()
        
    def __initInterface(self):
        self.resize(1000, 600)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')
        
        StyleSheet.SETTING.apply(self)
    
    def __createGroups(self):
        self.uiGroup = SettingCardGroup(self.tr("界面设置"))
        
    def __createCards(self):
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FluentIcon.BRUSH,
            self.tr("主题"),
            self.tr("切换亮色/暗色主题"),
            texts=[
                self.tr("亮色"),
                self.tr("暗色"),
                self.tr("跟随系统")
            ],
            parent=self.uiGroup
        )
    
    def __placeCards(self):
        self.uiGroup.addSettingCard(self.themeCard)
        
    def __initLayout(self):
        self.__createGroups()
        self.__createCards()
        self.__placeCards()
        
        self.expandLayout.setSpacing(20)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.uiGroup)
    
    def __connectSignals(self):
        cfg.themeChanged.connect(setTheme)