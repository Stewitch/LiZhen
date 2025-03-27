from qfluentwidgets import (qconfig, QConfig, OptionsConfigItem, Theme,
                            BoolValidator, OptionsValidator)



class LauncherConfig(QConfig):
    
    """启动器配置
    
    使用 qfluentwidgets 的 QConfig 类实现
    """
    
    # 控件缩放
    uiScale = OptionsConfigItem(
        "App", "uiScale", "Auto",
        OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"])
    )
    
    # 自动检查更新
    autoCheckUpdate = OptionsConfigItem(
        "App", "autoCheckUpdate", True,
        BoolValidator()
    )
    
    # 更新源
    updateSource = OptionsConfigItem(
        "App", "updateSource", "GitHub",
        OptionsValidator(["GitHub", "Gitee"])
    )
    
    # 首次启动
    firstStart = OptionsConfigItem(
        "App", "firstStart", True,
        BoolValidator()
    )
    
    # pip 镜像
    pipMirrorEnabled = OptionsConfigItem(
        "Mirror", "pipMirror", True,
        BoolValidator()
    )

    # HuggingFace 镜像
    hfMirrorEnabled = OptionsConfigItem(
        "Mirror", "hfMirror", True,
        BoolValidator()
    )
    


# 作为主程序模块导入时
if __name__ == "utils.config":
    
    from .path import UnchangeablePaths as UP
    from .log import logger
    
    launcherConfig = LauncherConfig()
    launcherConfig.themeMode.value = Theme.AUTO
    qconfig.load(
        UP.LAUNCHER_CFG, launcherConfig
    )
    
    logger.debug("启动器配置加载完成")