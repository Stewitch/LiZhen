from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Signal
from qfluentwidgets import (LineEdit, SettingCard, SpinBox, SwitchButton,
                            BodyLabel, PrimaryPushButton, PasswordLineEdit,
                            FluentIcon, DoubleSpinBox, ComboBox)
from pathlib import Path

from ..utils.bridge import Item
from ..utils.announce import broad
from ..utils.enums import Signals
from ..utils.log import logger



class SettingCard_(SettingCard):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self._item = item
        
        self._item.valueChanged.connect(lambda vs: self.setValue(vs[1]))
    
    def setValue(self, value):
        pass
    
    def value(self):
        return self._item.value
    
    def switchItem(self, item: Item):
        if item is self._item or item is None:
            return
        self._item = item
        self._item.valueChanged.connect(lambda vs: self.setValue(vs[1]))
        self.setValue(self._item.value)



class InputCard(SettingCard_):
    
    editingFinished = Signal(str)
    
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        
        self.lineEdit = LineEdit(self)
        self.lineEdit.setMinimumWidth(200)
        
        self.hBoxLayout.addWidget(self.lineEdit)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.lineEdit.editingFinished.connect(self.__onEditingFinished)
        
        
    def __onEditingFinished(self):
        text = self.lineEdit.text()
        self._item.set(text)
        self.editingFinished.emit(text)
        
    def setValue(self, value):
        self.lineEdit.setText(value)
        
    def setPlaceholder(self, text):
        self.lineEdit.setPlaceholderText(text)
        
    def text(self):
        return self.lineEdit.text()



class NumberCard(SettingCard_):
    
    valueChanged = Signal(float)
    
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        
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
        self.valueChanged.emit(float(value))
        
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

    def value(self):
        return self.spinBox.value()



class SwitchCard(SettingCard_):
    
    checkedChanged = Signal(bool)
    
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        
        self.switchButton = SwitchButton(self)
        
        self.switchButton.setOnText(self.tr("开"))
        self.switchButton.setOffText(self.tr("关"))
        
        self.hBoxLayout.addWidget(self.switchButton)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.switchButton.checkedChanged.connect(self.__onCheckedChanged)
    
    
    def __onCheckedChanged(self, checked):
        self._item.set(checked)
        self.checkedChanged.emit(checked)
    
    def setValue(self, value):
        self.switchButton.setChecked(value)
        
    def isChecked(self):
        return self.switchButton.isChecked()



class DisplayCard(SettingCard_):
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        
        self.bodyLabel = BodyLabel(self)
        
        self.hBoxLayout.addWidget(self.bodyLabel)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        

    def setValue(self, value):
        self.bodyLabel.setText(value)



class FolderCard(SettingCard_):
    
    folderChanged = Signal(Path)
    
    def __init__(self, item: Item, icon, title, content=None, caption=None, default=None, parent=None):
        super().__init__(item, icon, title, content, parent)
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
                self.folderChanged.emit(defalut)
        
        else:
            self._item.set(str(path))
            self.setValue(path)
            self.folderChanged.emit(path)
        


class PasswordInputCard(SettingCard_):
    
    editingFinished = Signal(str)
    
    def __init__(self, item: Item, icon, title, content=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        
        self.lineEdit = PasswordLineEdit(self)
        self.lineEdit.setMinimumWidth(200)
        
        self.hBoxLayout.addWidget(self.lineEdit)
        self.hBoxLayout.addSpacing(16)
        
        self.setValue(self._item.value)
        
        self.lineEdit.editingFinished.connect(self.__onEditingFinished)
        
        
    def __onEditingFinished(self):
        text = self.lineEdit.text()
        self._item.set(text)
        self.editingFinished.emit(text)
        
    def setValue(self, value):
        self.lineEdit.setText(value)
        
    def setPlaceholder(self, text):
        self.lineEdit.setPlaceholderText(text)
        
    def text(self):
        return self.lineEdit.text()



class OptionsCard(SettingCard_):
    
    currentIndexChanged = Signal(int)
    
    def __init__(self, item: Item, icon, title, content=None, options: list | tuple=None, parent=None):
        super().__init__(item, icon, title, content, parent)
        self.comboBox = ComboBox(self)
        self.comboBox.setMinimumWidth(200)
        
        self.hBoxLayout.addWidget(self.comboBox)
        self.hBoxLayout.addSpacing(16)
        
        if isinstance(options, (list, tuple)):
            self._options = options
            self.setOptions(options)
        else:
            self._options = []
        
        self.setValue(self._item.value)
        
        self.comboBox.currentIndexChanged.connect(self.__onCurrentIndexChanged)
        
    def setOptions(self, options: list | tuple):
        self._options = options
        self.comboBox.clear()
        self.comboBox.addItems(self._options)
        self.comboBox.setCurrentIndex(self._options.index(self._item.originalValue))
        
    def __onCurrentIndexChanged(self, index):
        self._item.set(self._options[index])
        self.currentIndexChanged.emit(index)
        
    def setValue(self, value):
        if value not in self._options:
            logger.warning(f"{value} 未在 {self._options} 中，无法设置")
            return
        self.comboBox.setCurrentIndex(self._options.index(value))
    
    def currentIndex(self):
        return self.comboBox.currentIndex()