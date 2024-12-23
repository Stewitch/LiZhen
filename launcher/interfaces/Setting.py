from qfluentwidgets import (SettingCardGroup, ScrollArea,
                            ComboBoxSettingCard, ExpandLayout, setTheme, SwitchSettingCard)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import InfoBar
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel

from ..utils.styles import StyleSheet
from ..utils.configs import cfg
from ..utils.logger import logger



class SettingInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.view = QWidget()
        self.expandLayout = ExpandLayout(self.view)

        # 标题标签
        self.settingLabel = QLabel(self.tr("设置"), self)

        # 界面设置组
        self.uiGroup = SettingCardGroup(self.tr('界面设置'), self.view)
        
        # 界面设置卡片
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
        self.zoomCard = ComboBoxSettingCard(
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
        
        # 镜像源设置卡片
        self.mirrorsGroup = SettingCardGroup(self.tr('镜像源设置'), self.view)
        self.pipMirrorEnabledCard = SwitchSettingCard(
            FIF.CLOUD_DOWNLOAD, self.tr("启用 pip 镜像源"),
            self.tr("pip 镜像源可以加速模块和依赖安装，建议国内用户开启"),
            configItem=cfg.pipMirrorEnabled, parent=self.mirrorsGroup)
        self.anacondaMirrorEnabledCard = SwitchSettingCard(
            FIF.CLOUD_DOWNLOAD, self.tr("启用 Anaconda 镜像源"),
            self.tr("解决 Anaconda 包下载失败等问题，建议国内用户开启"),
            configItem=cfg.anacondaMirrorEnabled, parent=self.mirrorsGroup)
        self.hfMirrorEnabledCard = SwitchSettingCard(
            FIF.CLOUD_DOWNLOAD, self.tr("启用 Hugging Face 镜像源"),
            self.tr("国内用户大多无法直接连接到 Hugging Face，启用镜像源可解决模型下载问题"),
            configItem=cfg.hfMirrorEnabled, parent=self.mirrorsGroup)

        self.__initWidget()

        logger.info("设置界面初始化完成")


    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        # 应用样式表
        self.view.setObjectName('view')
        self.settingLabel.setObjectName('settingLabel')
        StyleSheet.SETTING.apply(self)

        # 布局
        self.__initLayout()
        self.__connectSignalToSlot()


    def __initLayout(self):
        self.settingLabel.move(36, 30)

        # 组添加卡片
        self.uiGroup.addSettingCard(self.themeCard)
        self.uiGroup.addSettingCard(self.zoomCard)
        
        self.mirrorsGroup.addSettingCard(self.pipMirrorEnabledCard)
        self.mirrorsGroup.addSettingCard(self.anacondaMirrorEnabledCard)
        self.mirrorsGroup.addSettingCard(self.hfMirrorEnabledCard)

        # 布局添加组
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.uiGroup)
        self.expandLayout.addWidget(self.mirrorsGroup)


    def __restartAppNotice(self):
        InfoBar.success(
            self.tr('设置成功'),
            self.tr('重新打开启动器生效'),
            duration=1500,
            parent=self
        )

    def __restartProjectNotice(self):
        InfoBar.success(
            self.tr("设置成功"),
            self.tr("重启项目后生效"),
            duration=1000,
            parent=self
        )

    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__restartAppNotice)
        cfg.themeChanged.connect(setTheme)
        
        cfg.pipChanged.connect(self.__restartProjectNotice)
        cfg.anacondaChanged.connect(self.__restartProjectNotice)
        cfg.hfChanged.connect(self.__restartProjectNotice)
