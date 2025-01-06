from qfluentwidgets import qconfig, QConfig, OptionsConfigItem, OptionsValidator, Theme, BoolValidator

from .log import logger
from .paths import LAUNCHER_CONFIG



class LauncherConfig(QConfig):
    # UI
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    
    # Mirrors
    pipMirrorEnabled = OptionsConfigItem(
        "Mirrors", "pipEnabled", True, BoolValidator())
    hfMirrorEnabled = OptionsConfigItem(
        "Mirrors", "hfEnabled", True, BoolValidator())



cfg = LauncherConfig()
cfg.themeMode.value = Theme.AUTO
qconfig.load(LAUNCHER_CONFIG, cfg)
logger.info("启动器配置文件载入")