from PySide6.QtWidgets import QWidget

class Interface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)