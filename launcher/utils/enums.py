from qfluentwidgets import StyleSheetBase, Theme, qconfig
from enum import Enum

from .paths import QSS



class StyleSheet(StyleSheetBase, Enum):
    
    START = "Start"
    MANAGER = "Manager"
    
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return QSS.joinpath(f"{theme.value.lower()}/{self.value}.qss")



class Signals(Enum):
    
    showInfoBar = 0
    showWarnBar = 1
    showErrBar = 2
    showNoticeDialog = 3
    changeProjectFolder = 99

    agentUpdate = 1000
    llmProviderUpdate = 1001