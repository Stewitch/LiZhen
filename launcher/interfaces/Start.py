from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui.Ui_Start import Ui_Start

from ..utils.styles import StyleSheet
from ..utils.logger import logger
from ..utils.configs import pcfg



class StartInterface(QWidget, Ui_Start):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.__initFunctions()
        self.__initWidgets()
        
        logger.info(f"启动 界面初始化，对象名称：{self.objectName()}")
    
    
    def __initFunctions(self):
        logger.debug(pcfg.conf)
        self.ASR = pcfg.get("ASR_MODEL")
        self.LLM = pcfg.get("LLM_PROVIDER")
        self.TTS = pcfg.get("TTS_MODEL")
        self.ASRModel = pcfg.get(f"{self.ASR}.model_name", "详情页查看")
        self.LLMModel = pcfg.get(f"{self.LLM}.MODEL", "详情页查看")
        self.TTSModel = pcfg.get(f"{self.TTS}.voice", "详情页查看")
    
    
    def __initWidgets(self):
        self.ASRCard.setIcon("asr_available.png")
        self.ASRCard.title.setText(f"ASR:")
        self.ASRCard.provider.setText(f"{self.ASR}")
        self.ASRCard.model.setText(self.ASRModel)
        
        self.LLMCard.setIcon("llm.png")
        self.LLMCard.title.setText(f"LLM:")
        self.LLMCard.provider.setText(f"{self.LLM}")
        self.LLMCard.model.setText(f'{self.LLMModel}')
        
        self.TTSCard.setIcon("tts_available.png")
        self.TTSCard.title.setText(f"TTS:")
        self.TTSCard.provider.setText(f"{self.TTS}")
        self.TTSCard.model.setText(f"{self.TTSModel}")
        
        self.startButton.setIcon(FluentIcon.PLAY)
        
        self.ASRFolder.setIcon(FluentIcon.MICROPHONE)
        self.LLMFolder.setIcon(FluentIcon.MESSAGE)
        self.TTSFolder.setIcon(FluentIcon.VOLUME)
        self.personaFolder.setIcon(FluentIcon.FEEDBACK)
        
        self.setObjectName("StartInterface")
        StyleSheet.START.apply(self)
    
    
    
    