"""main.py
==================================================
Author: SunKSugaR
EMail: sunksugar@qq.com
GitHub: https://github.com/SunKSugaR
--------------------------------------------------
Description:
A launcher for Open-LLM-VTuber project.
Based on PySide6 and QFluentWidgets.

GitHub repository:
https://github.com/SunKSugaR/LiZhen
    
Open-LLM-VTuber:
https://github.com/t41372/Open-LLM-VTuber

QFluentWidgets:
https://qfluentwidgets.com/

License:
GNU General Public License v3.0
https://www.gnu.org/licenses/gpl-3.0.html
==================================================
Build:
See README.md
==================================================
Using Python 3.12.8
Code with passion, code with love.
"""



from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

from launcher.interfaces.MainWindow import MainWindow
from launcher.utils.configs import cfg
from launcher.utils.logger import logger
from launcher.utils.paths import FONTS
from launcher.utils.common import _launcher

import os, sys



if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))
    



def main():
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(str(FONTS.joinpath("Alibaba-PuHuiTi-Regular.ttf")))
    window = MainWindow()
    window.show()
    _launcher.switch()
    return app.exec()


if __name__ == '__main__':
    logger.info("主程序启动")
    code = main()
    logger.info("主程序退出")
    sys.exit(code)