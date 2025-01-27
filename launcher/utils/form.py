from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from typing import Dict, Tuple, List

from .mapping import CARDS_MAP, KEY_MAP, AVAILABLE_VALUES
from .bridge import Item, I18nMixin
from .log import logger
from .managers import itemManager
from .i18n import LANG



class SettingsForm(QObject):
    
    vDictChanged = Signal(dict)
    
    def __init__(self, config: I18nMixin, parent=None):
        super().__init__(parent)
        self.cfg = config
        self.infos: Dict[str, Tuple[QWidget, dict]] = {}
        self.cards: List[QWidget] = []
        
        self._init()
    
    
    @logger.catch
    def _init(self):
        for fieldName, fieldInfo in self.cfg.model_fields.items():
            try:
                if issubclass(fieldInfo.annotation, I18nMixin):
                    continue
            except TypeError:
                pass
                
            map = KEY_MAP.get(fieldName)
            if map is None:
                logger.warning(f"字段 {fieldName} 未在 KEY_MAP 中定义")
                continue
        
            item = Item(self.cfg, fieldName)
            itemManager.registerItem(item)
            
            icon = map.get("ico")
            title = map.get(LANG)
            content = self.cfg.get_field_description(fieldName, LANG)
            if title == content:
                content = None
            parent = self.parent()
            
            et = map.get("et")
            if et is not None:
                cardClass = CARDS_MAP.get(et)
            else:
                cardClass = CARDS_MAP.get(fieldInfo.annotation)
            
            card = cardClass(item, icon, title, content, parent)
            self.cards.append(card)
            self.infos[fieldName] = (card, map)
        
        self.__setCards()
    
    
    @logger.catch
    def __setCards(self):
        for fieldName, info in self.infos.items():
            card, map = info[0], info[1]
            if isinstance(card, CARDS_MAP.get("DIR")):
                card.setCaption(map.get("caption").get(LANG, self.tr("选择目录")))
                card.setDefault(map.get("default"))
            elif isinstance(card, CARDS_MAP.get(int)):
                card.setRange(map.get("range"))         
            elif isinstance(card, CARDS_MAP.get("OPTIONS")):
                options = AVAILABLE_VALUES.get(fieldName)
                logger.info(f"字段 {fieldName} 的可选值为 {options}")
                card.setOptions(options)
                
    
                
        