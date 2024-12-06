from interfaces.ui.Ui_Test import Ui_Test
from interfaces.Interface import Interface

class TestInterface(Interface, Ui_Test):
    def __init__(self, parent=None):
        super().__init__(parent)
