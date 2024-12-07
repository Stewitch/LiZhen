from interfaces.ui.Ui_Info import Ui_Info
from interfaces.Interface import Interface
from qfluentwidgets import FluentIcon

class InfoInterface(Interface, Ui_Info):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        # self.label.pixelFontSize = 14
        
        self.scrollArea.setStyleSheet("QScrollArea{background: transparent; border: none}")
        self.view.setStyleSheet("QWidget{background: transparent}")

        