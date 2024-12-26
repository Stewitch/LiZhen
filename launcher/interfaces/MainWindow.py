from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, QEventLoop, QTimer
from qfluentwidgets import FluentIcon, FluentWindow, NavigationItemPosition, SplashScreen

from .Info import InfoInterface
from .Setting import SettingInterface
from .Start import StartInterface
from .ASR import ASRInterface
from .LLM import LLMInterface
from .TTS import TTSInterface
from .Persona import PersonaInterface

from ..utils.logger import logger



class MainWindow(FluentWindow):
    @logger.catch
    def __init__(self):
        super().__init__()
        
        self.__initWindow()
        self.__splash()
        self.__initNavigation()
        self.__SSConnection()
        
        logger.info("主窗口初始化完成")
        QApplication.processEvents()
    
       
    def __initNavigation(self):
        
        self.startInterface = StartInterface(self)
        self.asrInterface = ASRInterface(self)
        self.llmInterface = LLMInterface(self)
        self.ttsInterface = TTSInterface(self)
        self.infoInterface = InfoInterface(self)
        self.settingInterface = SettingInterface(self)
        self.personaInterface = PersonaInterface(self)
        
        self.addSubInterface(self.startInterface, FluentIcon.PLAY, self.tr("启动"), NavigationItemPosition.TOP)
        self.navigationInterface.addSeparator()
        
        self.addSubInterface(self.asrInterface, FluentIcon.MICROPHONE, self.tr("ASR 管理"), NavigationItemPosition.SCROLL)
        self.addSubInterface(self.llmInterface, FluentIcon.MESSAGE, self.tr("LLM 管理"), NavigationItemPosition.SCROLL)
        self.addSubInterface(self.ttsInterface, FluentIcon.VOLUME, self.tr("TTS 管理"), NavigationItemPosition.SCROLL)
        self.addSubInterface(self.personaInterface, FluentIcon.FEEDBACK, self.tr("人格提示词管理"), NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator(NavigationItemPosition.BOTTOM)
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
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        self.splashScreen.finish()
    
    
    def __initWindow(self):
        self.setWindowTitle(self.tr("离真 启动器"))
        self.setWindowIcon(QIcon("./launcher/assets/images/LZ64.ico"))
        self.resize(1000, 700)
    
    
    def __SSConnection(self):
        self.startInterface.ASRCard.clicked.connect(lambda: self.switchTo(self.asrInterface))
        self.startInterface.LLMCard.clicked.connect(lambda: self.switchTo(self.llmInterface))
        self.startInterface.TTSCard.clicked.connect(lambda: self.switchTo(self.ttsInterface))