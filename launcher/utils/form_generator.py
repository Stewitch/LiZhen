from .paths import PROJ_SRC

import sys
sys.path.append(str(PROJ_SRC.absolute()))

from open_llm_vtuber.config_manager.utils import read_yaml, validate_config, save_config




from typing import Any, Dict, Type
from PySide6.QtWidgets import (QWidget, QFormLayout, QLineEdit, 
                             QSpinBox, QDoubleSpinBox, QCheckBox)
from pydantic import BaseModel

class ConfigFormGenerator:
    TYPE_WIDGET_MAP = {
        str: QLineEdit,
        int: QSpinBox,
        float: QDoubleSpinBox,
        bool: QCheckBox
    }
    
    def __init__(self, model: Type[BaseModel]):
        self.model = model 
        self.widgets: Dict[str, QWidget] = {}
        
    def create_form(self) -> QWidget:
        form = QWidget()
        layout = QFormLayout()
        form.setLayout(layout)
        
        # 遍历模型字段
        for field_name, field in self.model.model_fields.items():
            widget = self._create_widget(field_name, field)
            if widget:
                self.widgets[field_name] = widget
                layout.addRow(field.description or field_name.replace("_", " ").title(), widget)
                
        return form
    
    def _create_widget(self, field_name: str, field: Any) -> QWidget:
        widget_class = self.TYPE_WIDGET_MAP.get(field.annotation)
        if not widget_class:
            return None
            
        widget = widget_class()
        
        # 设置控件属性和验证
        if isinstance(widget, QDoubleSpinBox):
            widget.setRange(0, 1)
            widget.setDecimals(2)
            widget.setSingleStep(0.1)
        elif isinstance(widget, QSpinBox):
            widget.setRange(0, 100000)
                
        return widget
        
    def get_values(self) -> Dict[str, Any]:
        values = {}
        for field_name, widget in self.widgets.items():
            if isinstance(widget, QLineEdit):
                values[field_name] = widget.text()
            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                values[field_name] = widget.value()
            elif isinstance(widget, QCheckBox):
                values[field_name] = widget.isChecked()
        return values
        
    def set_values(self, data: Dict[str, Any]):
        for field_name, value in data.items():
            if widget := self.widgets.get(field_name):
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                    widget.setValue(value)
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(value)