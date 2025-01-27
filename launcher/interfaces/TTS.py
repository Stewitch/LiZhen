from qfluentwidgets import SettingCardGroup, FluentIcon

from .Interfaces import ManagerInterface
from .Cards import OptionsCard

from ..utils.bridge import Item, ttsConfig
from ..utils.i18n import LANG
from ..utils.mapping import AVAILABLE_VALUES, EXTRA_ENV_COMMANDS
from ..utils.managers import itemManager
from ..utils.form import SettingsForm
from ..utils.log import logger
from ..utils.announce import broad
from ..utils.enums import Signals


class TTSInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "TTS 管理"):
        super().__init__(parent, title, True)
    
    def _setGroups(self):
        self.modelGroup = SettingCardGroup(self.tr("模型选择"), self.view)
        self.detailGroup = SettingCardGroup(self.tr("模型设置"), self.view)
    
    def _setCards(self):
        self.modelCard = OptionsCard(
            Item(ttsConfig, "tts_model"),
            FluentIcon.MICROPHONE,
            self.tr("语音合成模型"),
            ttsConfig.get_field_description("tts_model", LANG),
            AVAILABLE_VALUES["tts_model"],
            self.modelGroup
        )
        item = self.modelCard._item
        itemManager.registerItem(item)
        cmd = EXTRA_ENV_COMMANDS.get(item.value)
        if cmd:
            broad.cast(Signals.extraCommand, cmd)
            logger.info(f"额外命令：{cmd}")
        
        self.detailForm = SettingsForm(
            getattr(ttsConfig, self.modelCard._item.value),
            self.detailGroup
        )
    
    def _addCards2Groups(self):
        self.modelGroup.addSettingCard(self.modelCard)
        self.detailGroup.addSettingCards(self.detailForm.cards)
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.modelGroup)
        self.expandLayout.addWidget(self.detailGroup)
    
    def _SSConnection(self):
        self.modelCard.currentIndexChanged.connect(self.__onModelChanged)
    
    def __onModelChanged(self, i):
        model = self.modelCard._options[i]
        settings = getattr(ttsConfig, model)
        logger.debug(f"TTS Model 变更: {model}")
        cmd = EXTRA_ENV_COMMANDS.get(model)
        if cmd:
            broad.cast(Signals.extraCommand, cmd)
            logger.info(f"额外命令：{cmd}")
        
        self.detailGroup.hide()
        self.detailGroup.setParent(None)
        
        if self.detailForm:
            for card in self.detailForm.cards:
                itemManager.unregisterItem(card._item)
        
        self.detailGroup = SettingCardGroup(self.tr("详细设置"), self.view)
        self.detailForm = SettingsForm(settings, self.detailGroup)
        self.detailGroup.addSettingCards(self.detailForm.cards)
        
        self.expandLayout.addWidget(self.detailGroup)
        self.detailGroup.show()