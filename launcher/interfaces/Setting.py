from qfluentwidgets import (SettingCardGroup, ComboBoxSettingCard, setTheme, 
                            setThemeColor, CustomColorSettingCard,
                            HyperlinkCard, PrimaryPushSettingCard)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import InfoBar

from .Interfaces import ManagerInterface

from ..utils.configs import cfg
from ..utils.log import logger
from ..utils.upgrade import Updater
from ..utils import VERSION

import sys



class SettingInterface(ManagerInterface):
    
    @logger.catch
    def __init__(self, parent=None, title: str = "设置"):
        self.updater = Updater()
        self.updater.setRepo(cfg.get(cfg.updateSource))
        if sys.executable.endswith("python.exe"):
            self.updater.setPythonRuntime()
        super().__init__(parent, title)
        
    
    def _setGroups(self):
        self.uiGroup = SettingCardGroup(self.tr('界面'), self.view)
        self.launcherGroup = SettingCardGroup(self.tr('启动器'), self.view)
    
    
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
        
        self.updateSourceCard = ComboBoxSettingCard(
            cfg.updateSource,
            FIF.CLOUD_DOWNLOAD,
            self.tr("更新仓库"),
            self.tr("选择使用 GitHub(国际) / Gitee(国内) 仓库进行更新"),
            ["GitHub", "Gitee"],
            self.launcherGroup
        )
        self.launcherInfoCard = PrimaryPushSettingCard(
            self.tr("检查更新"),
            FIF.INFO,
            self.tr("关于"),
            self.tr(f"© 2025, Stewitch，保留所有权利，当前版本：{VERSION}"),
            self.launcherGroup
        )
        self.launcherRepoCard = HyperlinkCard(
            "https://github.com/Stewitch/LiZhen",
            self.tr("前往 GitHub"),
            FIF.GITHUB,
            self.tr("Github 仓库"),
            self.tr("查看启动器源码，提交问题或建议"),
            self.launcherGroup
        )
        self.launcherLicenseCard = HyperlinkCard(
            "https://www.gnu.org/licenses/gpl-3.0.html",
            self.tr("查看协议"),
            FIF.DICTIONARY,
            self.tr("开源协议"),
            self.tr("本软件遵循 GPL-3.0 开源协议"),
            self.launcherGroup
        )
    
    
    def _addCards2Groups(self):
        self.uiGroup.addSettingCard(self.themeCard)
        self.uiGroup.addSettingCard(self.zoomCard)
        self.uiGroup.addSettingCard(self.themeColorCard)
        
        self.launcherGroup.addSettingCard(self.updateSourceCard)
        self.launcherGroup.addSettingCard(self.launcherInfoCard)
        self.launcherGroup.addSettingCard(self.launcherRepoCard)
        self.launcherGroup.addSettingCard(self.launcherLicenseCard)
    
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.uiGroup)
        self.expandLayout.addWidget(self.launcherGroup)
    
    
    def __restartAppNotice(self):
        InfoBar.success(
            self.tr('设置成功'),
            self.tr('重新打开 启动器 生效'),
            duration=1500,
            parent=self
        )
    
    def __showErrorBar(self, msg):
        InfoBar.error(
            self.tr("错误"),
            msg,
            parent=self
        )
        
    
    def _SSConnection(self):
        cfg.appRestartSig.connect(self.__restartAppNotice)
        cfg.themeChanged.connect(setTheme)
        cfg.themeChanged.connect(lambda: logger.info(f"主题更改为：{cfg.themeMode.value}"))
        cfg.themeColorChanged.connect(lambda c: setThemeColor(c))
        cfg.themeColorChanged.connect(lambda c: logger.info(f"主题颜色更新：{c}"))
        cfg.updateSource.valueChanged.connect(self.updater.setRepo)
        self.launcherInfoCard.button.clicked.connect(self.updater.exec)
        self.updater.showError.connect(self.__showErrorBar)
        
        