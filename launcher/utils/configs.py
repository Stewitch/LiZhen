from qfluentwidgets import qconfig, QConfig, OptionsConfigItem, OptionsValidator, Theme, BoolValidator

from ..utils.logger import logger
from ..utils.bridge import YamlConf

import os.path


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
    


if os.path.exists("conf.yaml"):
    pcfg = YamlConf("conf.yaml")



cfg = LauncherConfig()
cfg.themeMode.value = Theme.AUTO
qconfig.load('./launcher/configs/launcher.json', cfg)
logger.info("启动器配置文件载入")