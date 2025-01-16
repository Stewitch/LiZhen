from PySide6.QtCore import QObject, Signal
from typing import Any, List, Literal, Type, get_args
from pydantic import BaseModel
from copy import deepcopy

from .paths import PROJ_SRC, PROJ_CFG

import sys
sys.path.append(str(PROJ_SRC.absolute()))

from open_llm_vtuber.config_manager.utils import read_yaml, validate_config, save_config
from open_llm_vtuber.config_manager.main import I18nMixin



pcfg = validate_config(read_yaml(str(PROJ_CFG)))

systemConfig = pcfg.system_config



class ConfigHelper:
    @staticmethod
    def get_field_info(model: Type[BaseModel], field_path: str):
        """通过字段路径获取字段信息
        用法: get_field_info(pcfg, "character_config.agent_config.agent_settings.basic_memory_agent.llm_provider")
        """
        parts = field_path.split('.')
        current = model
        
        for part in parts[:-1]:
            current = getattr(current, part)
            
        return current.model_fields.get(parts[-1])
    
    @staticmethod 
    def get_literal_values(model: Type[BaseModel], field_path: str) -> List[Any]:
        """获取 Literal 类型字段的可用值"""
        field_info = ConfigHelper.get_field_info(model, field_path)
        if field_info and hasattr(field_info.annotation, "__origin__") and field_info.annotation.__origin__ is Literal:
            return list(get_args(field_info.annotation))
        return []



class Item(QObject):
    
    valueChanged = Signal(I18nMixin, str, tuple)
    
    def __init__(self, config: BaseModel, field: str):
        super().__init__()
        self.__cfg = config
        self.__field = field
        
        if not hasattr(self.__cfg, self.__field):
            raise ValueError(f"{self.__cfg} 中 不存在 字段 {self.__field}")

        self.__value = getattr(self.__cfg, self.__field)
        self.__ov = deepcopy(self.__value)
        
        self.setObjectName(f"Item_{self.__field}")
    
    
    def set(self, v):
        if self.__value == v:
            return
        self.__value = v
        setattr(self.__cfg, self.__field, v)
        self.valueChanged.emit(self.__cfg, self.__field, (self.__ov, v))
    
    
    @property
    def value(self):
        return self.__value
    
    
    @value.setter
    def value(self, v):
        self.set(v)
        
    
    def __repr__(self):
        return f"Item({self.__field}: {self.__value})"


def onSave(filepath):
    save_config(validate_config(pcfg.model_dump()), filepath)