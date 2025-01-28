from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, QEventLoop, QTimer
from qfluentwidgets import (FluentIcon, MSFluentWindow, NavigationItemPosition, SplashScreen, InfoBar)
from typing import List

from .Setting import SettingInterface
from .Start import StartInterface
from .ASR import ASRInterface
from .LLM import LLMInterface
from .TTS import TTSInterface
from .Character import CharacterInterface
from .Project import ProjectInterface
from .Console import ConsoleInterface
from .Widgets import StopDialog, SaveDialog, RestartDialog
from .Interfaces import ManagerInterface

from ..utils import VERSION, getVersion
from ..utils.log import logger
from ..utils.paths import IMAGES
from ..utils.configs import cfg
from ..utils.common import project, createShortcut
from ..utils.managers import itemManager
from ..utils.announce import broad
from ..utils.enums import Signals
from ..utils.bridge import saveConfig

import sys, subprocess



class MainWindow(MSFluentWindow):
    @logger.catch
    def __init__(self):
        super().__init__()
        
        self.__initWindow()
        self.__splash()
        self.__initNavigation()
        self.__SSConnection()
        
        logger.info("主窗口初始化完成")
        broad.cast(Signals.allInterfaceInited)
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
        
        self.managerInterfaces: List[ManagerInterface] = [
            self.asrInterface, self.llmInterface, self.ttsInterface,
            self.characterInterface, self.projectInterface
        ]
        
        
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
        self.settingInterface.updater.updateFinished.connect(self.__onUpdateFinished)
        
        for interface in self.managerInterfaces:
            interface.configsSave.connect(self.__configSave)
            interface.configsDiscard.connect(self.__configDiscard)
        
        project.tryToStop.connect(self.__tryToStop)
        
    
    def __tryToStop(self):
        stop = StopDialog(self.tr("项目正在启动！"), self.tr("是否停止项目运行？\n 可能需要重启启动器以再次启动项目！"), self)
        if stop.exec():
            project.stop()
        else:
            logger.info("用户取消停止项目")
        
    
    def __configSave(self):
        itemManager.onSave()
        logger.info("保存配置")
        dialog = SaveDialog(
            self.tr("保存配置"),
            self.tr("是否保存当前配置到conf.yaml?"),
            self
        )
        if dialog.exec():
            saveConfig()
            logger.info("已保存配置")
        else:
            for interface in self.managerInterfaces:
                interface.saveButton.setEnabled(True)

    
    def __configDiscard(self):
        itemManager.onDiscard()
        logger.info("已撤销上一个值变更")
    
    def __onUpdateFinished(self):
        if getVersion() == VERSION:
            InfoBar.success(
                self.tr("更新成功"),
                self.tr("启动器已是最新版本"),
                parent=self.settingInterface
            )
            return
        dialog = RestartDialog(
            self.tr("更新完成"),
            self.tr("是否重启启动器以应用更新？"),
            self
        )
        if dialog.exec():
            if itemManager.vDict != {}:
                s = SaveDialog(
                    self.tr("更新完成"),
                    self.tr("即将重启启动器，但当前有未保存的配置, 是否保存当前配置到conf.yaml?"),
                    self
                )
                if s.exec():
                    saveConfig()
                    logger.info("已保存配置")
                
            executable = sys.executable
            if executable.endswith("python.exe"):
                command = [executable, "main.py"]
            elif executable == "lizhen.exe":
                command = [executable]
            logger.info(f"重启启动器: {command}")
            subprocess.Popen(command)
            sys.exit(0)
        
    
    def closeEvent(self, e):
        sys.stderr = sys.__stderr__
        if itemManager.vDict != {}:
            s = StopDialog(
                self.tr("未保存配置"),
                self.tr("当前有未保存的配置, 是否继续关闭启动器？"),
                self
            )
            s.yesButton.setText(self.tr("取消关闭"))
            s.cancelButton.setText(self.tr("继续关闭"))
            if s.exec():
                e.ignore()
                return
        if project.isRunning() or project.isRunning() is None:
            stop = StopDialog(self.tr("项目正在运行！"), self.tr("如要退出启动器，请先停止项目运行！"), self)
            stop.yesButton.setText(self.tr("停止&退出"))
            if stop.exec():
                project._forceStop()
                e.accept()
            else:
                e.ignore()
                return
            
        if cfg.get(cfg.lFirtStart):
            w = StopDialog(
                self.tr("首次启动"),
                self.tr("这是您第一次启动启动器，是否创建桌面快捷方式？\n随后您也可以手动创建"),
                self
            )
            w.yesButton.setText(self.tr("创建"))
            w.cancelButton.setText(self.tr("不创建"))
            if w.exec():
                createShortcut()
            cfg.set(cfg.lFirtStart, False)
        logger.info("主窗口关闭")