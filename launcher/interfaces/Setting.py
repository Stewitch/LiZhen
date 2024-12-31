from qfluentwidgets import SettingCardGroup, ComboBoxSettingCard, setTheme, setThemeColor, SwitchSettingCard, CustomColorSettingCard
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import InfoBar

from .Interfaces import ManagerInterface

from ..utils.configs import cfg
from ..utils.logger import logger
from ..utils.common import pipMirrorFile



class SettingInterface(ManagerInterface):
    
    @logger.catch
    def __init__(self, parent=None, title = "设置"):
        super().__init__(parent, title)
        
    
    def _setGroups(self):
        self.uiGroup = SettingCardGroup(self.tr('界面设置'), self.view)
        self.mirrorsGroup = SettingCardGroup(self.tr('镜像源设置'), self.view)
    
    
    def _setCards(self):
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
        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FIF.PALETTE,
            self.tr('主题颜色'),
            self.tr('更改启动器主题颜色'),
            parent=self.uiGroup
        )
        
        self.pipMirrorEnabledCard = SwitchSettingCard(
            FIF.CLOUD_DOWNLOAD, self.tr("启用 pip 镜像源"),
            self.tr("pip 镜像源可以加速模块和依赖安装，建议国内用户开启"),
            configItem=cfg.pipMirrorEnabled,
            parent=self.mirrorsGroup)
        self.hfMirrorEnabledCard = SwitchSettingCard(
            FIF.CLOUD_DOWNLOAD, self.tr("启用 Hugging Face 镜像源"),
            self.tr("国内用户大多无法直接连接到 Hugging Face，启用镜像源可解决模型下载问题"),
            configItem=cfg.hfMirrorEnabled,
            parent=self.mirrorsGroup)
    
    
    def _addCards2Groups(self):
        self.uiGroup.addSettingCard(self.themeCard)
        self.uiGroup.addSettingCard(self.zoomCard)
        self.uiGroup.addSettingCard(self.themeColorCard)
        
        self.mirrorsGroup.addSettingCard(self.pipMirrorEnabledCard)
        self.mirrorsGroup.addSettingCard(self.hfMirrorEnabledCard)
    
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.uiGroup)
        self.expandLayout.addWidget(self.mirrorsGroup)
    
    
    def __restartAppNotice(self):
        InfoBar.success(
            self.tr('设置成功'),
            self.tr('重新打开 启动器 生效'),
            duration=1500,
            parent=self
        )
    
    
    def __restartProjectNotice(self):
        InfoBar.success(
            self.tr("设置成功"),
            self.tr("重启 项目 后生效"),
            duration=1000,
            parent=self
        )

    
    def _SSConnection(self):
        cfg.appRestartSig.connect(self.__restartAppNotice)
        cfg.themeChanged.connect(setTheme)
        cfg.themeColorChanged.connect(lambda c: setThemeColor(c))
        
        cfg.pipMirrorEnabled.valueChanged.connect(self.__restartProjectNotice)
        cfg.pipMirrorEnabled.valueChanged.connect(lambda v: pipMirrorFile(v))
        cfg.hfMirrorEnabled.valueChanged.connect(self.__restartProjectNotice)
        