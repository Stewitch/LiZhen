from pathlib import Path

import os.path


# 工作区
CWD = Path(os.getcwd())
# 启动器主文件夹
LAUNCHER = CWD.joinpath('launcher')
# 项目文件夹
PROJECT = CWD.joinpath('Open-LLM-VTuber')


# 项目主文件
RUN_PROJECT = PROJECT.joinpath('run_server.py')
# 项目虚拟环境
VENV = PROJECT.joinpath('.venv')
# 激活脚本
VENV_ACTIVATE = VENV.joinpath('Scripts').joinpath('activate')


# 资源相关
ASSETS = LAUNCHER.joinpath('assets')
I18N = ASSETS.joinpath('i18n')
IMAGES = ASSETS.joinpath('images')
QSS = ASSETS.joinpath('qss')
FONTS = ASSETS.joinpath('fonts')
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
    print(VENV_ACTIVATE)
    os.system(f"cmd /k {VENV_ACTIVATE}") 