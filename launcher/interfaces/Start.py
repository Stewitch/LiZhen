from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui.Ui_Start import Ui_Start

from ..utils.enums import StyleSheet
from ..utils.log import logger
from ..utils.common import switchProjectState, openFolder, project

pcfg = {}

class StartInterface(QWidget, Ui_Start):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.__initFunctions()
        self.__initWidgets()
        self.__SSConnection()
        
        logger.info(f"启动 界面初始化，对象名称：{self.objectName()}")
    
    
    def __initFunctions(self):
        self.ASR = pcfg.get("ASR_MODEL")
        self.LLM = pcfg.get("LLM_PROVIDER")
        self.TTS = pcfg.get("TTS_MODEL")
        self.ASRModel = pcfg.get(f"{self.ASR}.model_name", "详情页查看")
        self.LLMModel = pcfg.get(f"{self.LLM}.MODEL", "详情页查看")
        self.TTSModel = pcfg.get(f"{self.TTS}.voice", "详情页查看")
    
    
    def __initWidgets(self):
        self.ASRCard._init("asr_available.png", f"ASR:", f"{self.ASR}", f"{self.ASRModel}")
        self.LLMCard._init("llm.png", f"LLM:", f"{self.LLM}", f"{self.LLMModel}")
        self.TTSCard._init("tts_available.png", f"TTS:", f"{self.TTS}", f"{self.TTSModel}")
  
        self.startButton.setIcon(FluentIcon.PLAY_SOLID)
        self.toConsoleButton.setIcon(FluentIcon.COMMAND_PROMPT)
        
        self.ASRFolder.setIcon(FluentIcon.MICROPHONE)
        self.LLMFolder.setIcon(FluentIcon.MESSAGE)
        self.TTSFolder.setIcon(FluentIcon.VOLUME)
        self.personaFolder.setIcon(FluentIcon.FEEDBACK)
        
        self.setObjectName("StartInterface")
        StyleSheet.START.apply(self)
    
    
    def __updateButton(self, status: str):
        try:
            if status in ["on", "starting"]:
                self.startButton.setText("终止项目！")
                self.startButton.setIcon(FluentIcon.PAUSE_BOLD)
            else:
                self.startButton.setText("一键启动！")
                self.startButton.setIcon(FluentIcon.PLAY_SOLID)
        except KeyboardInterrupt:
            self.__updateButton(status)
    
    
    def __SSConnection(self):
        project.changed.connect(self.__updateButton)
        self.startButton.clicked.connect(switchProjectState)
        self.ASRFolder.clicked.connect(openFolder)
        self.LLMFolder.clicked.connect(openFolder)
        self.TTSFolder.clicked.connect(openFolder)
        self.personaFolder.clicked.connect(openFolder)
    

