from qfluentwidgets import SettingCardGroup, FluentIcon

from .Interfaces import ManagerInterface
from .Widgets import InputCard, PasswordInputCard, SwitchCard, OptionsCard

from ..utils.form_generator import llm_config



class LLMInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "LLM 管理"):
        super().__init__(parent, title, True)
        self.currentLLM = None
    
    
    def _setGroups(self):
        self.detailsGroup = SettingCardGroup(self.tr("详细设置"), self.view)
    
    
    def _setCards(self):
        self.llmProviderCard = OptionsCard(
            FluentIcon.MESSAGE,
            self.tr("")
        )
        self.baseUrlCard = InputCard(
            FluentIcon.LINK,
            self.tr("API 链接"),
            self.tr("输入 LLM 后端的 API 链接"),
            self.tr("http://localhost:11434/v1"),
            llm_config.llm_provider,
            self.detailsGroup
        )
        self.APIKeyCard = PasswordInputCard(
            FluentIcon.VPN,
            self.tr("API 密钥"),
            self.tr("访问后端链接的 API 密钥"),
            self.tr("somethingelse"),
            self.detailsGroup
        )
        self.organizationCard = InputCard(
            FluentIcon.CAFE,
            self.tr("组织 ID"),
            self.tr("如果你不知道填什么，保持默认即可"),
            self.tr("org_eternity"),
            self.detailsGroup
        )
        self.projectCard = InputCard(
            FluentIcon.FLAG,
            self.tr("项目 ID"),
            self.tr("如果你不知道填什么，保持默认即可"),
            self.tr("project_glass"),
            self.detailsGroup
        )
        self.modelNameCard = InputCard(
            FluentIcon.IOT,
            self.tr("模型名称"),
            self.tr("输入模型名称"),
            self.tr("qwen2.5:latest"),
            self.detailsGroup
        )
        self.verboseCard = SwitchCard(
            FluentIcon.ALIGNMENT,
            self.tr("详细输出"),
            self.tr("启用详细输出"),
            self.detailsGroup
        )
    
    
    def _addCards2Groups(self):
        self.detailsGroup.addSettingCards([
            self.baseUrlCard,
            self.APIKeyCard,
            self.modelNameCard,
            self.organizationCard,
            self.projectCard,
            self.verboseCard
        ])
    
    
    def _addGroups2Layout(self):
        super()._addGroups2Layout()
        self.expandLayout.addWidget(self.detailsGroup)
    
        