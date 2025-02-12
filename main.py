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
https://github.com/Stewitch/LiZhen

Gitee repository:
https://gitee.com/Stewitch/LiZhen
    
Open-LLM-VTuber:
https://github.com/Open-LLM-VTuber/Open-LLM-VTuber

QFluentWidgets:
https://qfluentwidgets.com/

License:
GNU General Public License v3.0
https://www.gnu.org/licenses/gpl-3.0.html

afdian:
https://afdian.com/a/Stewitch
==================================================
Build:
See README.md
==================================================
Using Python 3.12.8
Code with passion, code with love.
"""



from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QFontDatabase

from launcher.interfaces.MainWindow import MainWindow
from launcher.interfaces.Widgets import StopDialog
from launcher.utils.configs import cfg
from launcher.utils.common import createShortcut
from launcher.utils.log import logger
from launcher.utils.paths import FONTS

import os, sys, traceback



def setup_environment():
    try:
        logger.info(f"当前工作目录: {os.getcwd()}")
        # logger.info(f"Python路径: {sys.executable}")
        # logger.info(f"系统路径: {sys.path}")
        
        if cfg.get(cfg.dpiScale) != "Auto":
            os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
            os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))
        
        # 确保关键目录存在
        # os.makedirs(FONTS, exist_ok=True)
        # logger.info(f"字体目录: {FONTS}")
        
    except Exception as e:
        logger.error(f"环境设置失败: {e}")
        logger.error(traceback.format_exc())


@logger.catch
def main():
    try:
        logger.info("正在初始化QApplication...")
        app = QApplication(sys.argv)
        
        # 检查字体文件
        font_path = FONTS.joinpath("Alibaba-PuHuiTi-Regular.ttf")
        if not font_path.exists():
            error_msg = f"找不到字体文件: {font_path}"
            logger.error(error_msg)
            QMessageBox.critical(None, "错误", error_msg)
            return 1
        
        logger.info("正在加载字体...")
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id < 0:
            error_msg = "字体加载失败"
            logger.error(error_msg)
            QMessageBox.critical(None, "错误", error_msg)
            return 1
            
        logger.info("正在创建主窗口...")
        window = MainWindow()
        window.show()
        
        logger.info("进入主循环...")
        if cfg.get(cfg.lFirtStart):
            w = StopDialog(
                window.tr("首次启动"),
                window.tr("这是您第一次运行启动器，是否创建桌面快捷方式？\n随后您也可以在设置中手动选择创建"),
                window
            )
            w.yesButton.setText(window.tr("创建"))
            w.cancelButton.setText(window.tr("不创建"))
            if w.exec():
                createShortcut()
            cfg.set(cfg.lFirtStart, False)
        return app.exec()
        
    except Exception as e:
        error_msg = f"程序启动失败: {e}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        QMessageBox.critical(None, "错误", error_msg)
        return 1



if __name__ == '__main__':
    logger.info("主程序启动")
    setup_environment()
    sys.exit(main())
    