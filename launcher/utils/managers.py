from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from typing import List, Dict, Any, Iterable

from .bridge import Item
from .log import logger



class ItemManager(QObject):
    
    vDictChanged = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.items: List[Item] = []
        self.registeredItems: Dict[str, Item] = {}
        self.vDict: Dict[str, Any] = {}
    
    def addItem(self, item: Item):
        self.items.append(item)
        item.valueChanged.connect(lambda _, item=item:self._valueDict(item))
    
    def registerItem(self, item: Item):
        self.registeredItems[item.field] = item
        if item not in self.items:
            self.addItem(item)
    
    def _valueDict(self, fieldOrItem: str | Item):
        if isinstance(fieldOrItem, str):
            item = self.registeredItems.get(fieldOrItem)
            field = item.field
        else:
            item = fieldOrItem
            field = item.field
        
        if item in self.registeredItems.values():
            if item.originalValue == item.value:
                self.vDict.pop(field)
            else:
                self.vDict[field] = item.value
            self.vDictChanged.emit(self.vDict)
            logger.debug(f"配置值表变更：{self.vDict}")
            
        else:
            logger.warning(f"未注册配置项：{item}, 尝试注册")
            self.registerItem(item)
            self._valueDict(item)
            
        
    def onSave(self):
        for item in self.items:
            item.onSave()
        self.vDict = {}
        self.vDictChanged.emit(self.vDict)
    
    def onDiscard(self):
        for item in self.items:
            item.onDiscard()
        self.vDict = {}
        self.vDictChanged.emit(self.vDict)
        


itemManager = ItemManager()



class InterfaceManager(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.interfaces = {}
    
    def addInterface(self, interface: QWidget | Iterable[QWidget]):
        if isinstance(interface, Iterable):
            for i in interface:
                self.interfaces[i.objectName()] = i
        elif isinstance(interface, QWidget):
            self.interfaces[interface.objectName()] = interface
        else:
            logger.warning(f"{interface} 不是 QWidget 子类实例或其实例列表")
    
    def getInterface(self, name):
        return self.interfaces.get(name)
    
    def removeInterface(self, name):
        self.interfaces.pop(name, None)
    
    def clear(self):
        self.interfaces.clear()
        
    def __iter__(self):
        return iter(self.interfaces.values())
    
    def __getitem__(self, name):
        return self.interfaces[name]
    
    def __setitem__(self, name, value):
        self.interfaces[name] = value
    
    def __delitem__(self, name):
        self.interfaces.pop(name)
    
    def __len__(self):
        return len(self.interfaces)
    
    def __contains__(self, name):
        return name in self.interfaces



interfaceManager = InterfaceManager()