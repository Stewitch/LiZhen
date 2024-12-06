from interfaces.ui.Ui_Info import Ui_Info
from interfaces.Interface import Interface

class InfoInterface(Interface, Ui_Info):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # self.label.pixelFontSize = 14

