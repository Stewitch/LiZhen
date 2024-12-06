from qfluentwidgets import *
from .Test import TestInterface
from .Info import InfoInterface

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fluent Window")
        self.setFixedSize(900, 600)
        
        self.testInterface = TestInterface(self)
        self.infoInterface = InfoInterface(self)
        
        self.addSubInterface(self.infoInterface, FluentIcon.INFO, "信息")
        self.addSubInterface(self.testInterface, FluentIcon.DEVELOPER_TOOLS, "测试")
        
        self.testInterface.pushButton.clicked.connect(common.toggleTheme)
        