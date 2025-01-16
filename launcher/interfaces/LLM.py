from PySide6.QtCore import Signal
from qfluentwidgets import SettingCardGroup, InfoBadge, InfoBadgePosition, InfoLevel

from .Interfaces import ManagerInterface

from ..utils.form import SettingsForm
from ..utils.bridge import systemConfig
from ..utils.log import logger



class LLMInterface(ManagerInterface):
    
    badgeUpdate = Signal(int)
    
    def __init__(self, parent=None, title = "LLM 管理"):
        super().__init__(parent, title, True)
        self.cfg = systemConfig
        self.settingsForm = SettingsForm(systemConfig, self)
        self.detailsGroup = SettingCardGroup("", self.view)
        self.detailsGroup.addSettingCard(self.settingsForm)
        self.expandLayout.addWidget(self.detailsGroup)
        
        self.settingsForm.vDictChanged.connect(self.onVDictChanged)
    
    def onVDictChanged(self, dict):
        logger.info(f"配置变更: {dict}")
        if len(dict) > 0:
            self.saveButton.setEnabled(True)
        else:
            self.saveButton.setEnabled(False)
