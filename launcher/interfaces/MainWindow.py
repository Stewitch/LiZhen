from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, QEventLoop, QTimer
from qfluentwidgets import (FluentIcon, MSFluentWindow, NavigationItemPosition, SplashScreen)

from .Setting import SettingInterface
from .Start import StartInterface
from .ASR import ASRInterface
from .LLM import LLMInterface
from .TTS import TTSInterface
from .Character import CharacterInterface
from .Project import ProjectInterface
from .Console import ConsoleInterface
from .Widgets import StopDialog

from ..utils.log import logger
from ..utils.paths import IMAGES
from ..utils.common import project
from ..utils.managers import interfaceManager

import sys



class MainWindow(MSFluentWindow):
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
        self.settingInterface = SettingInterface(self)
        self.characterInterface = CharacterInterface(self)
        self.consoleInterface = ConsoleInterface(self)
        self.projectInterface = ProjectInterface(self)
        
        interfaceManager.addInterface([
            self.asrInterface, self.ttsInterface, self.characterInterface,
            self.projectInterface,
        ])
        
        
        self.addSubInterface(
            self.startInterface, FluentIcon.PLAY, self.tr("启动"),
            selectedIcon=FluentIcon.PLAY_SOLID,
            position=NavigationItemPosition.TOP
        )
        
        
        self.addSubInterface(
            self.projectInterface, FluentIcon.DEVELOPER_TOOLS, self.tr("项目"),
            selectedIcon=FluentIcon.DEVELOPER_TOOLS,
            position=NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.characterInterface, FluentIcon.FEEDBACK, self.tr("角色"),
            selectedIcon=FluentIcon.FEEDBACK,
            position=NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.asrInterface, FluentIcon.MICROPHONE, self.tr("ASR"),
            selectedIcon=FluentIcon.MICROPHONE,
            position=NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.llmInterface, FluentIcon.MESSAGE, self.tr("LLM"),
            selectedIcon=FluentIcon.MESSAGE,
            position=NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.ttsInterface, FluentIcon.VOLUME, self.tr("TTS"),
            selectedIcon=FluentIcon.VOLUME,
            position=NavigationItemPosition.SCROLL
        )
        
        
        self.addSubInterface(
            self.consoleInterface, FluentIcon.COMMAND_PROMPT, self.tr("控制台"),
            selectedIcon=FluentIcon.COMMAND_PROMPT,
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.settingInterface, FluentIcon.SETTING, self.tr("设置"),
            selectedIcon=FluentIcon.SETTING,
            position=NavigationItemPosition.BOTTOM
        )
    
    
    def __splash(self):
        self.splashScreen = SplashScreen(str(IMAGES.joinpath("lz128.ico")), self)
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
        self.setWindowIcon(QIcon(str(IMAGES.joinpath("lz64.ico"))))
        self.resize(1000, 700)
    
    
    def __SSConnection(self):
        self.startInterface.ASRCard.clicked.connect(lambda: self.switchTo(self.asrInterface))
        self.startInterface.LLMCard.clicked.connect(lambda: self.switchTo(self.llmInterface))
        self.startInterface.TTSCard.clicked.connect(lambda: self.switchTo(self.ttsInterface))
        self.startInterface.toConsoleButton.clicked.connect(lambda: self.switchTo(self.consoleInterface))
        self.startInterface.toSettingButton.clicked.connect(lambda: self.switchTo(self.settingInterface))
        

        project.tryToStop.connect(self.__tryToStop)
        
    
    def __tryToStop(self):
        stop = StopDialog(self.tr("项目正在启动！"), self.tr("是否停止项目运行？\n 可能需要重启启动器以再次启动项目！"), self)
        if stop.exec():
            project.stop()
        else:
            logger.info("用户取消停止项目")
        
    
    def __configSave(self):
        logger.info("保存配置")

    
    def __configDiscard(self):
        logger.info("放弃配置")
        
    
    def closeEvent(self, e):
        sys.stderr = sys.__stderr__
        if project.isRunning() or project.isRunning() is None:
            stop = StopDialog(self.tr("项目正在运行！"), self.tr("如要退出启动器，请先停止项目运行！"), self)
            stop.yesButton.setText(self.tr("停止&退出"))
            if stop.exec():
                project._forceStop()
                e.accept()
            else:
                e.ignore()
        logger.info("主窗口关闭")