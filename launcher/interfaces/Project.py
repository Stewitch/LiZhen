from PySide6.QtCore import Signal
from qfluentwidgets import SettingCardGroup, SwitchSettingCard, FluentIcon, InfoBar

from .Interfaces import ManagerInterface

from ..utils.form import SettingsForm
from ..utils.bridge import systemConfig
from ..utils.configs import cfg
from ..utils.announce import broad
from ..utils.common import pipMirrorFile, project



class ProjectInterface(ManagerInterface):
    
    
    def __init__(self, parent=None, title = "项目设置"):
        super().__init__(parent, title, True)


    def _setGroups(self):
        self.systemGroup = SettingCardGroup("系统", self.view)
        self.commonsGroup = SettingCardGroup(self.tr("常规 (即时保存)"), self.view)
    
    
    def _setCards(self):
        self.checkEnvCard = SwitchSettingCard(
            FluentIcon.CHECKBOX,
            "强制环境检测",
            "每次启动时强制检测项目虚拟环境",
            cfg.checkEnv,
            self.commonsGroup
        )
        self.checkEnvCard.switchButton.setEnabled(False)
        
        self.pipMirrorEnabledCard = SwitchSettingCard(
            FluentIcon.CLOUD_DOWNLOAD,
            self.tr("启用 pip 镜像源"),
            self.tr("pip 镜像源可以加速模块和依赖安装，建议国内用户开启"),
            configItem=cfg.pipMirrorEnabled,
            parent=self.commonsGroup
        )
        self.hfMirrorEnabledCard = SwitchSettingCard(
            FluentIcon.CLOUD_DOWNLOAD,
            self.tr("启用 Hugging Face 镜像源"),
            self.tr("国内用户大多无法直接连接到 Hugging Face，启用镜像源可解决模型下载问题"),
            configItem=cfg.hfMirrorEnabled,
            parent=self.commonsGroup
        )
        
        self.systemForm = SettingsForm(systemConfig, self.systemGroup)
    
    
    def _addCards2Groups(self):
        self.commonsGroup.addSettingCard(self.checkEnvCard)
        self.commonsGroup.addSettingCard(self.pipMirrorEnabledCard)
        self.commonsGroup.addSettingCard(self.hfMirrorEnabledCard)
        self.systemGroup.addSettingCards(self.systemForm.cards)
        
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.commonsGroup)
        self.expandLayout.addWidget(self.systemGroup)
        
    
    def _SSConnection(self):
        
        broad.showErrBar.connect(self._showErrorBar)
        broad.showWarnBar.connect(self._showWarnBar)
        broad.showInfoBar.connect(self._showInfoBar)
        
        cfg.pipMirrorEnabled.valueChanged.connect(self.__restartProjectNotice)
        cfg.pipMirrorEnabled.valueChanged.connect(lambda v: pipMirrorFile(v))
        cfg.hfMirrorEnabled.valueChanged.connect(self.__restartProjectNotice)
        
    
    def __restartProjectNotice(self):
        if not project.isRunning():
            return
        InfoBar.success(
            self.tr("设置成功"),
            self.tr("重启 项目 后生效"),
            duration=1000,
            parent=self
        )
    

