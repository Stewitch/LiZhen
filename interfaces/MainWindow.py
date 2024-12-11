from qfluentwidgets import FluentIcon, FluentWindow, NavigationItemPosition, SplashScreen
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, QEventLoop, QTimer
from .Info import InfoInterface
from .Setting import SettingInterface

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        
        self.__initWindow()
        self.__splash()
        self.__initNavigation()
        
        QApplication.processEvents()
        
    def __initNavigation(self):
        
        self.infoInterface = InfoInterface(self)
        self.settingInterface = SettingInterface(self)
        
        self.addSubInterface(self.infoInterface, FluentIcon.INFO, self.tr("信息"), NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FluentIcon.SETTING, self.tr("设置"), NavigationItemPosition.BOTTOM)
        
    def __splash(self):
        self.splashScreen = SplashScreen("./launcher/assets/images/LZ128.ico", self)
        self.splashScreen.setIconSize(QSize(128, 128))
        
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        
        self.show()
        loop = QEventLoop(self)
        QTimer.singleShot(2000, loop.quit)
        loop.exec()
        self.splashScreen.finish()
    
    def __initWindow(self):
        self.setWindowTitle(self.tr("离真 启动器"))
        self.setWindowIcon(QIcon("./launcher/assets/images/LZ64.ico"))
        self.resize(1000, 600)