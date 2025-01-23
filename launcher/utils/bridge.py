from PySide6.QtCore import QObject, Signal
from pydantic import BaseModel
from copy import deepcopy

from .paths import PROJ_SRC, PROJ_CFG

import sys
sys.path.append(str(PROJ_SRC.absolute()))

from open_llm_vtuber.config_manager.utils import read_yaml, validate_config, save_config
from open_llm_vtuber.config_manager.main import I18nMixin



pcfg = validate_config(read_yaml(str(PROJ_CFG)))

systemConfig = pcfg.system_config
characterConfig = pcfg.character_config
agentConfig = characterConfig.agent_config
basicMemoryAgentConfig = agentConfig.agent_settings.basic_memory_agent
humeAIConfig = agentConfig.agent_settings.hume_ai_agent
asrConfig = characterConfig.asr_config



class Item(QObject):
    
    valueChanged = Signal(tuple)
    
    def __init__(self, config: BaseModel, field: str):
        super().__init__()
        self.__cfg = config
        self.__field = field
        
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
        self.set(v)
        
    
    def __repr__(self):
        return f"Item({self.__field}: {self.__value})"


def saveConfig():
    save_config(pcfg, str(PROJ_CFG))
    
