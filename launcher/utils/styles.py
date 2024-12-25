from qfluentwidgets import StyleSheetBase, Theme, qconfig
from enum import Enum

class StyleSheet(StyleSheetBase, Enum):
    
    SETTING = "Setting"
    MANAGER = "Manager"
    
    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"./launcher/assets/qss/{theme.value.lower()}/{self.value}.qss"