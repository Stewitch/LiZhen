from PySide6.QtCore import Signal, QObject

from .mapping import CARDS_MAP, KEY_MAP
from .bridge import Item, I18nMixin



LANG = "zh"



class SettingsForm(QObject):
    
    vDictChanged = Signal(dict)
    
    def __init__(self, config: I18nMixin, parent=None):
        super().__init__(parent)
        self.cfg = config
        self.infos = {}
        self.vDict = {}
        self.cards = []
        
        self._init()
    
    
    def _init(self):
        for fieldName, fieldInfo in self.cfg.model_fields.items():
            map = KEY_MAP.get(fieldName)
            if map is None:
                continue
        
            item = Item(self.cfg, fieldName)
            item.valueChanged.connect(
                lambda _, field, values: self._valueDict(field, values)
            )
            
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
    
    
    def __setCards(self):
        for _, info in self.infos.items():
            card, map = info[0], info[1]
            if isinstance(card, CARDS_MAP.get("DIR")):
                card.setCaption(map.get("caption").get(LANG, self.tr("选择目录")))
                card.setDefault(map.get("default"))
            elif isinstance(card, CARDS_MAP.get("INT")) or isinstance(card, CARDS_MAP.get(int)):
                card.setRange(map.get("range"))
            
                
                
        
    def _valueDict(self, field, values):
        # values: (old, new)
        self.vDict[field] = values
        if values[0] == values[1]:
            self.vDict.pop(field, None)
        self.vDictChanged.emit(self.vDict)
        