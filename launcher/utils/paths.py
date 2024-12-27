from pathlib import Path

import os.path


# 工作区
CWD = Path(os.getcwd())
# 启动器主文件夹
LAUNCHER = CWD.joinpath('launcher')
# 项目文件夹
PROJECT = CWD.joinpath('Open-LLM-VTuber')


# 资源相关
ASSETS = LAUNCHER.joinpath('assets')
I18N = ASSETS.joinpath('i18n')
IMAGES = ASSETS.joinpath('images')
QSS = ASSETS.joinpath('qss')
UICONS = IMAGES.joinpath('ui')


# 配置文件
CONFIGS = LAUNCHER.joinpath('configs')
LAUNCHER_CONFIG = CONFIGS.joinpath('launcher.json')
MIRRORS = CONFIGS.joinpath('mirrors.json')


# 日志文件
LOGS = LAUNCHER.joinpath('logs')
LAUNCHER_LOG = LOGS.joinpath('launcher.log')


if __name__ == "__main__":
    print(CWD)
    print(LAUNCHER)
    os.startfile(LAUNCHER)