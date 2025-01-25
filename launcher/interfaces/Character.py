from qfluentwidgets import SettingCardGroup, FluentIcon

from .Interfaces import ManagerInterface
from .Cards import OptionsCard

from ..utils.form import SettingsForm
from ..utils.bridge import characterConfig, Item, agentConfig, agentSettings
from ..utils.mapping import AVAILABLE_VALUES
from ..utils.managers import itemManager
from ..utils.log import logger
from ..utils.announce import broad
from ..utils.enums import Signals



class CharacterInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "角色设定"):
        super().__init__(parent, title, True)
           
    
    def _setGroups(self):
        self.characterGroup = SettingCardGroup("角色设定", self.view)
        self.agentGroup = SettingCardGroup("AI代理", self.view)
    
    
    def _setCards(self):
        self.characterForm = SettingsForm(characterConfig, self.characterGroup)
        self.agentCard = OptionsCard(
            Item(agentConfig, "conversation_agent_choice"),
            FluentIcon.ROBOT,
            self.tr("对话代理"),
            self.tr("选择要使用的AI对话代理"),
            AVAILABLE_VALUES["conversation_agent_choice"],
            self.agentGroup
        )
        itemManager.registerItem(self.agentCard._item)
        self.agentForm = SettingsForm(
            getattr(
                agentSettings, itemManager.getByField("conversation_agent_choice").value
            ),
            self.agentGroup)
        
    def _addCards2Groups(self):
        self.characterGroup.addSettingCards(self.characterForm.cards)
        self.agentGroup.addSettingCard(self.agentCard)
        self.agentGroup.addSettingCards(self.agentForm.cards)
    
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.characterGroup)
        self.expandLayout.addWidget(self.agentGroup)
        
    
    def _SSConnection(self):
        itemManager.getByField("conversation_agent_choice").valueChanged.connect(self._onAgentChange)
    
    
    def _onAgentChange(self, v):
        logger.debug(f"Agent 变更: {v[0]} -> {v[1]}")
        
        settings = getattr(agentSettings, v[1])
        logger.debug(f"{v[1]} 配置项: {settings}")
        
        self.expandLayout.removeWidget(self.agentGroup)

        self.agentGroup.hide()
        self.agentGroup.setParent(None)
        
        for card in self.agentForm.cards:
            itemManager.unregisterItem(card._item)
        
        self.agentForm = SettingsForm(settings, self.agentGroup)
        
        self.agentGroup = SettingCardGroup("AI代理", self.view)
        self.agentGroup.addSettingCard(self.agentCard)
        self.agentGroup.addSettingCards(self.agentForm.cards)
        self.expandLayout.addWidget(self.agentGroup)
        self.agentGroup.show()
        
        if hasattr(settings, "llm_provider"):
            self.agentForm.infos["llm_provider"][0]._item.valueChanged.connect(
                lambda p: broad.cast(Signals.llmProviderUpdate, p)
            )
