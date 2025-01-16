from qfluentwidgets import GroupHeaderCardWidget, BodyLabel
from PySide6.QtCore import Signal

from .mapping import WIDGETS_MAP, KEY_MAP, WIDGETS_SIZE
from .bridge import ConfigHelper, Item, I18nMixin
from .log import logger


LANG = "zh"


class SettingsForm(GroupHeaderCardWidget):
    
    vDictChanged = Signal(dict)
    
    def __init__(self, config: I18nMixin, parent=None):
        super().__init__(parent)
        self.infos = {}
        self.cfg = config
        self.vDict = {}
        
        self.setTitle("详细设置")
        self.setBorderRadius(8)
        
        self._init()
        
    def _init(self):
        for fieldName, fieldInfo in self.cfg.model_fields.items():
            map = KEY_MAP.get(fieldName)
            if map is None:
                continue
            item = Item(self.cfg, fieldName)
            et =  map.get("et")
            if et is not None:
                widget = WIDGETS_MAP.get(et)()
            else:
                widget = WIDGETS_MAP.get(fieldInfo.annotation)()
            self.infos[fieldName] = (widget, map, item)
            self.addGroup(map["ico"], map[LANG], self.cfg.get_field_description(fieldName, LANG), widget)
        
        self.setMinimumHeight(len(self.infos) * 62 + 36)
        
        self._initWidgets()
            
    
    def _initWidgets(self):
        for widget, map, item in self.infos.values():
            # 使用默认参数来固定当前循环的item值
            item.valueChanged.connect(
                lambda cfg, field, values: self._valueDict(field, values)
            )
            
            widget.setMinimumWidth(WIDGETS_SIZE[widget.__class__])
            
            if isinstance(item.value, str):
                widget.setText(item.value)
                if not isinstance(widget, BodyLabel):
                    # 使用默认参数来固定当前循环的item值
                    widget.textChanged.connect(
                        lambda v, item=item: item.set(v)
                    )
                    logger.info(f"{widget} 的 textChanged Signal 连接至 Slot {item} 上")
            elif isinstance(item.value, bool):
                widget.setOnText(self.tr("开"))
                widget.setOffText(self.tr("关"))
                widget.setChecked(item.value)
                widget.checkedChanged.connect(
                    lambda v, item=item: item.set(v)
                )
                logger.info(f"{widget} 的 checkedChanged Signal 连接至 Slot {item} 上")
            elif isinstance(item.value, int):
                r = map.get("range")
                if r:
                    widget.setRange(r[0], r[1])
                widget.setValue(item.value)
                widget.valueChanged.connect(
                    lambda v, item=item: item.set(v)
                )
                logger.info(f"{widget} 的 valueChanged Signal 连接至 Slot {item} 上")
        
    
    def _valueDict(self, field, values):
        # values: (old, new)
        self.vDict[field] = values
        if values[0] == values[1]:
            self.vDict.pop(field, None)
        self.vDictChanged.emit(self.vDict)
        