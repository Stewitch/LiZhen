"""main.py
=============================================
Author: SunKSugaR
EMail: sunksugar@qq.com
GitHub: https://github.com/SunKSugaR
---------------------------------------------
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
=============================================
"""



from PySide6.QtWidgets import QApplication
from interfaces.MainWindow import MainWindow
from utils.configs import cfg
import os

if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

def main():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()