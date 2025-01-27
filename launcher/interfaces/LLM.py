from qfluentwidgets import SettingCardGroup, FluentIcon

from .Interfaces import ManagerInterface
from .Cards import DisplayCard

from ..utils.bridge import statelessLLMConfigs, agentConfig, agentSettings, Item
from ..utils.announce import broad
from ..utils.form import SettingsForm
from ..utils.log import logger
from ..utils.managers import itemManager



class LLMInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "LLM 管理"):
        super().__init__(parent, title, True)
        broad.agentUpdate.connect(self.__onAgentUpdate)
        broad.llmProviderUpdate.connect(self.__onProviderUpdate)
    
    
    def _setGroups(self):
        self.llmGroup = SettingCardGroup(self.tr("详细设置"), self.view)
        self.tipGroup = SettingCardGroup(self.tr("提示"), self.view)
    
    def _setCards(self):
        self.tipCard = DisplayCard(
            Item(agentConfig, "conversation_agent_choice"),
            FluentIcon.HELP,
            self.tr("当前对话代理"),
            self.tr("本页一般仅在使用 Basic Memory Agent 时有用"),
            self.tipGroup
        )
        self.providerCard = DisplayCard(
            Item(agentConfig.agent_settings.basic_memory_agent, "llm_provider"),
            FluentIcon.CHAT,
            self.tr("大语言模型后端"),
            self.tr("本项在 角色 - AI代理 - 大语言模型后端 处设置，此处仅为展示"),
            self.tipGroup
        )
        if agentConfig.conversation_agent_choice == "basic_memory_agent":
            self.llmForm = SettingsForm(
                getattr(
                    statelessLLMConfigs, agentSettings.basic_memory_agent.llm_provider
                ),
                self.llmGroup
            )
        else:
            self.llmForm = None
    
    def _addCards2Groups(self):
        self.tipGroup.addSettingCard(self.tipCard)
        self.tipGroup.addSettingCard(self.providerCard)
        if agentConfig.conversation_agent_choice == "basic_memory_agent":
            self.llmGroup.addSettingCards(self.llmForm.cards)
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.tipGroup)
        self.expandLayout.addWidget(self.llmGroup)
        
    
    def __onAgentUpdate(self, agent: str):
        if agent == "basic_memory_agent":
            self.tipCard.setValue(self.tr("当前：")+f"{agent}")
            self.providerCard.setValue(self.providerCard._item.value)
            self.llmGroup.show()
        else:
            self.tipCard.setValue(self.tr("当前：")+f"{agent}")
            self.providerCard.setValue("None")
            self.llmGroup.hide()

    
    def __onProviderUpdate(self, provider: str):
        logger.debug(f"LLM Provider 变更: {provider}")
        settings = getattr(statelessLLMConfigs, provider)
        self.providerCard.switchItem(itemManager.registeredItems.get("llm_provider"))
        self.llmGroup.hide()
        self.llmGroup.setParent(None)
        
        if self.llmForm:
            for card in self.llmForm.cards:
                itemManager.unregisterItem(card._item)
        
        self.llmGroup = SettingCardGroup(self.tr("详细设置"), self.view)
        self.llmForm = SettingsForm(settings, self.llmGroup)
        self.llmGroup.addSettingCards(self.llmForm.cards)
        
        self.expandLayout.addWidget(self.llmGroup)
        self.llmGroup.show()