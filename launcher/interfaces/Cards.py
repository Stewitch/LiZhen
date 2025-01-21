from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import (LineEdit, SettingCard, SpinBox, SwitchButton,
                            BodyLabel, PrimaryPushButton, PasswordLineEdit,
                            FluentIcon, DoubleSpinBox)
from pathlib import Path

from ..utils.bridge import Item
from ..utils.announce import broad
from ..utils.enums import Signals



class InputCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        self.lineEdit = LineEdit(self)
        self.lineEdit.setMinimumWidth(200)
        
        self.hBoxLayout.addWidget(self.lineEdit)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.lineEdit.editingFinished.connect(self.__onEditingFinished)
        
        
    def __onEditingFinished(self):
        self._item.set(self.lineEdit.text())
        
    def setValue(self, value):
        self.lineEdit.setText(value)
        
    def setPlaceholder(self, text):
        self.lineEdit.setPlaceholderText(text)



class NumberCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        if isinstance(self._item.value, float):
            self.spinBox = DoubleSpinBox(self)
            self.setRange((0.0, 999999.0))
        else:
            self.spinBox = SpinBox(self)
            self.setRange((0, 999999))
        self.spinBox.setMinimumWidth(150)
        
        self.hBoxLayout.addWidget(self.spinBox)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.spinBox.valueChanged.connect(self.__onValueChanged)
        
        
    def __onValueChanged(self, value):
        self._item.set(value)
        
    def setValue(self, value):
        self.spinBox.setValue(value)
        
    def setRange(self, range: tuple):
        try:
            min, max = range[0], range[1]
            if min >= max:
                min, max = 0, 999999
        except:
            min, max = 0, 999999
        self.spinBox.setRange(min, max)
        
    def setStep(self, step):
        self.spinBox.setSingleStep(step)



class SwitchCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        self.switchButton = SwitchButton(self)
        
        self.hBoxLayout.addWidget(self.switchButton)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.switchButton.checkedChanged.connect(self.__onCheckedChanged)
    
    
    def __onCheckedChanged(self, checked):
        self._item.set(checked)
    
    def setValue(self, value):
        self.switchButton.setChecked(value)



class DisplayCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        self.bodyLabel = BodyLabel(self)
        
        self.hBoxLayout.addWidget(self.bodyLabel)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        

    def setValue(self, value):
        self.bodyLabel.setText(value)



class FolderCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, caption=None, default=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        self._caption = caption
        self._default = default
        
        self.pushButton = PrimaryPushButton(self)
        self.pushButton.setMinimumWidth(150)
        self.pushButton.setIcon(FluentIcon.FOLDER)
        
        self.hBoxLayout.addWidget(self.pushButton)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.pushButton.clicked.connect(self.__onClicked)
        
    def setCaption(self, text):
        self._caption = text
        
    def setDefault(self, path):
        self._default = path
    
    def setValue(self, value):
        if not isinstance(value, Path):
            value = Path(value)
        self.pushButton.setText(self.tr("已选择:")+value.name)
        self.pushButton.setChecked(True)
    
    
    def __selectFolder(self):
        from ..utils.paths import PROJECT
        return QFileDialog.getExistingDirectory(self, self._caption, str(PROJECT))
    
    def __checkFolder(self, path):
        try:
            path = Path(path)
            if not path.exists():
                raise
            if str(path) == ".":
                return
            return path
        except:
            return False
    
    def __onClicked(self):
        path = self.__checkFolder(self.__selectFolder())
        if path is None:
            broad.cast(Signals.showInfoBar, self.tr("已取消选择！"))
            return
        if not path:
            defalut = self.__checkFolder(self._default)
            if not defalut:
                broad.cast(Signals.showErrBar, self.tr("选择路径以及默认路径均不存在"))
                self.pushButton.setChecked(False)
                self.pushButton.setText(self.tr("未选择"))
                return
            else:
                broad.cast(Signals.showWarnBar, self.tr("目录无效，设置为默认目录"))
                self._item.set(str(defalut))
                self.setValue(defalut)
        
        else:
            self._item.set(str(path))
            self.setValue(path)
        


class PasswordInputCard(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        self.lineEdit = PasswordLineEdit(self)
        self.lineEdit.setMinimumWidth(200)
        
        self.hBoxLayout.addWidget(self.lineEdit)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.lineEdit.editingFinished.connect(self.__onEditingFinished)
        
        
    def __onEditingFinished(self):
        self._item.set(self.lineEdit.text())
        
    def setValue(self, value):
        self.lineEdit.setText(value)
        
    def setPlaceholder(self, text):
        self.lineEdit.setPlaceholderText(text)


