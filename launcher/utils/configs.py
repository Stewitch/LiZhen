from qfluentwidgets import (qconfig, QConfig, OptionsConfigItem, OptionsValidator,
                            Theme, BoolValidator)

from PySide6.QtCore import Signal

from ..utils.logger import logger


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
    
    @logger.catch
    def set(self, item, value, save=True, copy=True):
        logger.debug("./launcher/configs/launcher.json 更新")
        if item is self.pipMirrorEnabled:
            self.pipChanged.emit()
        elif item is self.anacondaMirrorEnabled:
            self.anacondaChanged.emit()
        elif item is self.hfMirrorEnabled:
            self.hfChanged.emit()
        return super().set(item, value, save, copy)


cfg = LauncherConfig()
cfg.themeMode.value = Theme.AUTO
qconfig.load('./launcher/configs/launcher.json', cfg)