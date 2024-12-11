# coding:utf-8

from qfluentwidgets import (qconfig, QConfig, OptionsConfigItem, OptionsValidator,
                            Theme, BoolValidator)

from PySide6.QtCore import Signal

class LauncherConfig(QConfig):

    # UI
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    
    # Mirrors
    pipMirrorEnabled = OptionsConfigItem(
        "Mirrors", "pipEnabled", True, BoolValidator())
    anacondaMirrorEnabled = OptionsConfigItem(
        "Mirrors", "anacondaEnabled", True, BoolValidator())
    hfMirrorEnabled = OptionsConfigItem(
        "Mirrors", "hfEnabled", True, BoolValidator())
    
    pipChanged = Signal()
    anacondaChanged = Signal()
    hfChanged = Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def set(self, *args, **kwargs):
        super().set(*args, **kwargs)
        item = args[0]
        match item:
            case self._cfg.anacondaChanged:
                self.anacondaChanged.emit()
            case self._cfg.pipChanged:
                self.pipChanged.emit()
            case self._cfg.hfChanged:
                self.hfChanged.emit()



cfg = LauncherConfig()
cfg.themeMode.value = Theme.AUTO
qconfig.load('./launcher/configs/config.json', cfg)