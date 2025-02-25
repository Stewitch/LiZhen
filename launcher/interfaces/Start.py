from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon, MessageBox

from .ui.Ui_Start import Ui_Start
from .Widgets import FirstStartDialog, SaveDialog

from ..utils.enums import StyleSheet
from ..utils.log import logger
from ..utils.common import switchProjectState, openFolder, project
from ..utils.announce import broad
from ..utils.managers import itemManager
from ..utils.bridge import statelessLLMConfigs
from ..utils.configs import cfg

import webbrowser


class StartInterface(QWidget, Ui_Start):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.ASR = None
        self.LLM = None
        self.TTS = None
        self.ASRModel = "详情页查看"
        self.LLMModel = "详情页查看"
        self.TTSModel = "详情页查看"
        self.agent = None
        self.l2d = None
        self.character = None
        
        self.__initWidgets()
        self.__SSConnection()
        
        logger.info(f"启动 界面初始化，对象名称：{self.objectName()}")
    
    
    def __initWidgets(self):
        self.ASRCard._init("asr_available.png", f"ASR:", f"{self.ASR}", f"{self.ASRModel}")
        self.LLMCard._init("llm.png", f"LLM:", f"{self.LLM}", f"{self.LLMModel}")
        self.TTSCard._init("tts_available.png", f"TTS:", f"{self.TTS}", f"{self.TTSModel}")
  
        self.startButton.setIcon(FluentIcon.PLAY_SOLID)
        self.toConsoleButton.setIcon(FluentIcon.COMMAND_PROMPT)
        self.toSettingButton.setIcon(FluentIcon.SETTING)
        
        self.ASRFolder.setIcon(FluentIcon.MICROPHONE)
        self.LLMFolder.setIcon(FluentIcon.MESSAGE)
        self.TTSFolder.setIcon(FluentIcon.VOLUME)
        self.personaFolder.setIcon(FluentIcon.FEEDBACK)
        
        self.pFolders.setVisible(False)
        
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
    
    
    def __checkConfig(self):
        if itemManager.vDict != {}:
            s = SaveDialog(
                self.tr("未保存配置"),
                self.tr("当前有未保存的配置, 保存以继续启动或取消并返回修改"),
                self
            )
            if s.exec():
                itemManager.onSave()
                return True
            else:
                return False
        return True
            
    
    def __onProjectStart(self):
        if cfg.get(cfg.firstStart):
            dialog = FirstStartDialog(
                self.tr("首次启动"),
                self.tr("*仅对于N卡用户：*请确认已按照文档配置了 CUDA&CUDNN\n 对于所有用户：请确保已按照文档配置了FFMpeg和除虚拟环境之外的项目"),
                self
            )
            if dialog.exec():
                if not webbrowser.open("https://open-llm-vtuber.github.io/docs/quick-start#%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87"):
                    w = MessageBox(
                        self.tr("链接打开失败"),
                        self.tr("请手动前往: https://open-llm-vtuber.github.io/docs/quick-start#%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87"),
                        self
                    )
                return
            else:
                cfg.set(cfg.firstStart, False)
                if not self.__checkConfig():
                    return
                switchProjectState()
        else:
            if not self.__checkConfig():
                return
            switchProjectState()
    
    def __SSConnection(self):
        itemManager.saved.connect(self.__updateConfig)
        project.changed.connect(self.__updateButton)
        self.startButton.clicked.connect(self.__onProjectStart)
        self.ASRFolder.clicked.connect(openFolder)
        self.LLMFolder.clicked.connect(openFolder)
        self.TTSFolder.clicked.connect(openFolder)
        self.personaFolder.clicked.connect(openFolder)
        broad.allInterfaceInited.connect(self.__updateConfig)
        broad.agentUpdate.connect(self.__onAgentUpdate)
        broad.llmProviderUpdate.connect(self.__onProviderUpdate)
    
    
    def __updateWidgets(self):
        self.ASRCard.updateInfo(self.ASR, self.ASRModel)
        self.LLMCard.updateInfo(self.LLM, self.LLMModel)
        self.TTSCard.updateInfo(self.TTS, self.TTSModel)
        self.characterName.setText(self.character)
        self.l2dName.setText(self.l2d)
        self.agentName.setText(self.agent)
    
    
    @logger.catch
    def __updateConfig(self):
        self.ASR = itemManager.registeredItems["asr_model"].value
        model = itemManager.registeredItems.get("model_name")
        self.ASRModel = model.value if model else "详情页查看"
        self.agent = itemManager.registeredItems["conversation_agent_choice"].value
        
        self.__onAgentUpdate(self.agent)
        
        self.TTS = itemManager.registeredItems["tts_model"].value
        model = itemManager.registeredItems.get("voice")
        self.TTSModel = model.value if model else "详情页查看"
        self.character = itemManager.getByField("conf_name").value
        self.l2d = itemManager.getByField("live2d_model_name").value
        
        self.__updateWidgets()
    
    
    def __onAgentUpdate(self, agent):
        if agent == "basic_memory_agent":
            llm = itemManager.registeredItems["llm_provider"].value
            self.__onProviderUpdate(llm)
            
        else:
            self.LLM = agent
            self.LLMModel = "详情页查看"
            self.LLMCard.updateInfo(self.LLM, self.LLMModel)
        self.agentName.setText(agent)
            
    def __onProviderUpdate(self, llm):
        self.LLM = llm
        self.LLMModel = itemManager._cFieldItems.get(f"{getattr(statelessLLMConfigs, llm).__repr_name__()}.model").value
        self.LLMCard.updateInfo(self.LLM, self.LLMModel)
    

