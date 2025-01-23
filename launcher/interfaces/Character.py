from qfluentwidgets import SettingCardGroup, FluentIcon

from .Interfaces import ManagerInterface
from .Cards import OptionsCard

from ..utils.form import SettingsForm
from ..utils.bridge import characterConfig, Item, agentConfig
from ..utils.mapping import AVAILABLE_VALUES
from ..utils.managers import itemManager



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
        
    def _addCards2Groups(self):
        self.characterGroup.addSettingCards(self.characterForm.cards)
        self.agentGroup.addSettingCard(self.agentCard)
    
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.characterGroup)
        self.expandLayout.addWidget(self.agentGroup)
        
    
    def _SSConnection(self):
        itemManager.registerItem(self.agentCard._item)