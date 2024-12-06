from qfluentwidgets import *
from interfaces.Test import TestInterface

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fluent Window")
        
        self.testInterface = TestInterface(self)
        self.addSubInterface(self.testInterface, FluentIcon.DEVELOPER_TOOLS, "测试子界面")
        
        self.testInterface.pushButton.clicked.connect(common.toggleTheme)
        
        