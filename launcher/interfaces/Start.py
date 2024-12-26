from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui.Ui_Start import Ui_Start

from ..utils.styles import StyleSheet
from ..utils.logger import logger



class StartInterface(QWidget, Ui_Start):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.__initFunctions()
        self.__initWidgets()
        
        logger.info(f"启动 界面初始化，对象名称：{self.objectName()}")
    
    
    def __initFunctions(self):
        self.ASR = None
        self.LLM = None
        self.TTS = None
    
    
    def __initWidgets(self):
        self.ASRCard.setIcon("asr_available.png")
        self.ASRCard.title.setText(f"ASR:\n{self.ASR}")
        
        self.LLMCard.setIcon("llm.png")
        self.LLMCard.title.setText(f"LLM:\n{self.LLM}")
        
        self.TTSCaed.setIcon("tts_available.png")
        self.TTSCaed.title.setText(f"TTS:\n{self.TTS}")
        
        self.startButton.setIcon(FluentIcon.PLAY)
        
        self.ASRFolder.setIcon(FluentIcon.MICROPHONE)
        self.LLMFolder.setIcon(FluentIcon.MESSAGE)
        self.TTSFolder.setIcon(FluentIcon.VOLUME)
        self.personaFolder.setIcon(FluentIcon.FEEDBACK)
        
        self.setObjectName("StartInterface")
        StyleSheet.START.apply(self)
    