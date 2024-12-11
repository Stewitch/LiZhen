# coding:utf-8
from qfluentwidgets import (SettingCardGroup, OptionsSettingCard, ScrollArea,
                            ComboBoxSettingCard, ExpandLayout, setTheme)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import InfoBar
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel


from utils.styles import StyleSheet
from utils.configs import cfg

HELP_URL = ""
FEEDBACK_URL = ""
AUTHOR = ""
VERSION = ""
YEAR = ""

class SettingInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.view = QWidget()
        self.expandLayout = ExpandLayout(self.view)

        # setting label
        self.settingLabel = QLabel(self.tr("设置"), self)

        # 界面设置
        self.uiGroup = SettingCardGroup(
            self.tr('界面设置'), self.view)
        self.themeCard = ComboBoxSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr('主题'),
            self.tr("选择 亮色/暗色 主题"),
            texts=[
                self.tr('亮色'), self.tr('暗色'),
                self.tr('跟随系统')
            ],
            parent=self.uiGroup
        )
        self.zoomCard = OptionsSettingCard(
            cfg.dpiScale,
            FIF.ZOOM,
            self.tr("界面缩放"),
            self.tr("更改文字、控件的缩放比例"),
            texts=[
                "100%", "125%", "150%", "175%", "200%",
                self.tr("使用系统设置")
            ],
            parent=self.uiGroup
        )
        self.languageCard = ComboBoxSettingCard(
            cfg.language,
            FIF.LANGUAGE,
            self.tr('语言'),
            self.tr('选择 UI 语言'),
            texts=['简体中文', '繁體中文', 'English', self.tr('使用系统设置')],
            parent=self.uiGroup
        )



        self.__initWidget()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        # initialize style sheet
        self.view.setObjectName('view')
        self.settingLabel.setObjectName('settingLabel')
        StyleSheet.SETTING.apply(self)


        # initialize layout
        self.__initLayout()
        self.__connectSignalToSlot()

    def __initLayout(self):
        self.settingLabel.move(36, 30)

        # add cards to group
        self.uiGroup.addSettingCard(self.themeCard)
        self.uiGroup.addSettingCard(self.zoomCard)
        self.uiGroup.addSettingCard(self.languageCard)


        # add setting card group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.uiGroup)


    def __showRestartTooltip(self):
        """ show restart tooltip """
        InfoBar.success(
            self.tr('设置成功'),
            self.tr('重启应用后生效'),
            duration=1500,
            parent=self
        )


    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        # personalization
        cfg.themeChanged.connect(setTheme)
