from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from pydantic import BaseModel
from copy import deepcopy

from .paths import PROJ_CFG
from .log import logger

try:
    from ..open_llm_vtuber.config_manager.utils import read_yaml, validate_config, save_config
    from ..open_llm_vtuber.config_manager.main import I18nMixin
except:
    QMessageBox.critical(
        None, "错误", "项目路径有误，请检查后重试！",
        QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.NoButton
    )
    logger.critical("项目路径有误，请检查后重试！")
    raise
    


pcfg = validate_config(read_yaml(str(PROJ_CFG)))

systemConfig = pcfg.system_config
port = systemConfig.port
characterConfig = pcfg.character_config
agentConfig = characterConfig.agent_config
agentSettings = agentConfig.agent_settings
statelessLLMConfigs = agentConfig.llm_configs
asrConfig = characterConfig.asr_config
ttsConfig = characterConfig.tts_config



class Item(QObject):
    
    valueChanged = Signal(tuple)
    
    def __init__(self, config: BaseModel, field: str):
        super().__init__()
        self.__cfg = config
        self.__field = field
        self.cfield = f"{config.__repr_name__()}.{field}"
        
        if not hasattr(self.__cfg, self.__field):
            raise ValueError(f"{self.__cfg} 中 不存在 字段 {self.__field}")

        self.__value = getattr(self.__cfg, self.__field)
        self.__ov = deepcopy(self.__value)
        
        self.setObjectName(f"Item_{self.__field}")
    
    
    def set(self, v, copy=True):
        if self.__value == v:
            return
        self.__value = deepcopy(v) if copy else v
        setattr(self.__cfg, self.__field, v)
        self.valueChanged.emit((self.__ov, v))
        
    def onSave(self):
        self.__ov = deepcopy(self.__value)
    
    def onDiscard(self):
        self.set(self.__ov)
    
    
    @property
    def value(self):
        return self.__value
    
    @property
    def field(self):
        return self.__field
    
    @property
    def originalValue(self):
        return self.__ov
    
    @property
    def config(self):
        return self.__cfg
    
    @value.setter
    def value(self, v):
        """
        警告：
            属性修改器仅用于特殊情况下值的修改
            不会触发 ItemManager._valueDict 在内的特殊方法
            如需修改配置，请用 Item.set 方法
        """
        self.value = deepcopy(v)
        
    
    def __repr__(self):
        return f"Item({self.__field}: {self.__value})"



def saveConfig():
    save_config(pcfg, PROJ_CFG)
    

logger.info('配置桥接初始化完成')