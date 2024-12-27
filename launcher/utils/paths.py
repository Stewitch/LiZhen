from pathlib import Path

import os.path


# 工作区
CWD = Path(os.getcwd())
# 启动器主文件夹
LAUNCHER = CWD.joinpath('launcher')

# 资源相关
ASSETS = LAUNCHER.joinpath('assets')
I18N = ASSETS.joinpath('i18n')
IMAGES = ASSETS.joinpath('images')
QSS = ASSETS.joinpath('qss')

# 配置文件




if __name__ == "__main__":
    print(CWD)
    print(LAUNCHER)
    os.startfile(LAUNCHER)