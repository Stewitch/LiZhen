from interfaces.ui.Ui_test import Ui_Test
from PySide6.QtWidgets import QWidget

class TestInterface(QWidget, Ui_Test):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
