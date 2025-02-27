from PySide6.QtCore import QObject, Signal
from typing import List, Dict, Any

from .bridge import Item
from .log import logger



class ItemManager(QObject):
    
    vDictChanged = Signal(dict)
    saved = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.items: List[Item] = []
        self.registeredItems: Dict[str, Item] = {}
        self._cFieldItems: Dict[str, Item] = {}
        self.vDict: Dict[str, Any] = {}
        self.changedFields: List[str] = []
    
    def addItem(self, item: Item):
        self.items.append(item)
        item.valueChanged.connect(lambda _, item=item:self._valueDict(item))
    
    def registerItem(self, item: Item):
        self.registeredItems[item.field] = item
        self._cFieldItems[item.cfield] = item
        if not item in self.items:
            self.addItem(item)
    
    def unregisterItem(self, item: Item):
        try:
            self.registeredItems.pop(item.field)
            self.items.pop(self.items.index(item))
        except ValueError:
            logger.warning(f"未注册配置项：{item}")
        except KeyError:
            logger.warning(f"未注册配置项：{item}")
    
    def getByField(self, field: str) -> Item:
        return self.registeredItems.get(field, None)
    
    def _valueDict(self, fieldOrItem: str | Item):
        if isinstance(fieldOrItem, str):
            item = self.registeredItems.get(fieldOrItem)
            field = item.field
        else:
            item = fieldOrItem
            field = item.field
        
        if item in self.registeredItems.values():
            if item.originalValue == item.value:
                try:
                    self.vDict.pop(field)
                    self.changedFields.pop(self.changedFields.index(field))
                except ValueError:
                    logger.debug("撤销操作触发 _valueDict")
            else:
                self.vDict[field] = item.value
                self.changedFields.append(item.field)
            self.vDictChanged.emit(self.vDict)
            logger.debug(f"配置值表变更：{self.vDict}")
            logger.debug(f"变更的键：{self.changedFields}")
            
        else:
            logger.warning(f"未注册配置项：{item}, 尝试注册")
            self.registerItem(item)
            self._valueDict(item)
            
        
    def onSave(self):
        if self.vDict == {}:
            return
        for item in self.items:
            item.onSave()
        self.vDict = {}
        self.vDictChanged.emit(self.vDict)
        self.saved.emit()
    
    def onDiscard(self):
        if self.vDict == {}:
            self.changedFields = []
            return
        try:
            field = self.changedFields.pop()
        except Exception as e:
            logger.warning(f"{e}")
            return
        self.registeredItems.get(field).onDiscard()
        self.vDict.pop(field, None)
        self.vDictChanged.emit(self.vDict)
        


itemManager = ItemManager()

logger.info('配置项管理器初始化完成')