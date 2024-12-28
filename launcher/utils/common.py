from PySide6.QtGui import QColor
from PySide6.QtCore import QObject, Signal, QTimer

from .logger import logger

import os, subprocess



class Status(QObject):
    
    changed = Signal(str)

    def __init__(self, status: str = "off"):
        super().__init__()
        self.__status = status
    
    
    def isRunning(self):
        if self.__status == "starting":
            return None
        return self.__status == "on"
    
    
    def switch(self):
        if self.isRunning():
            self.__status = "off"
        elif self.__status == "starting":
            self.__status = "on"
        else:
            self.__status = "starting"
        self.changed.emit(self.__status)
    
    
    def changeTo(self, s: str):
        if s in ["off", "starting", "on"] and self.__status != s:
            self.__status = s
            self.changed.emit(self.__status)
            
    
    def __str__(self):
        return self.__status
        
    


_project = Status()
_launcher = Status()



class Color:
    RED = QColor(255, 0, 0)
    GREEN = QColor(0, 255, 0)
    BLUE = QColor(0, 0, 255)
    LIME_GREEN = QColor(50, 205, 50)
    GOLD = QColor(255, 215, 0)



def openFolder(folder: str):
    if not isinstance(folder, str):
        logger.error(f"文件夹路径错误：{folder}")
        return
    logger.debug(f"打开文件夹：{folder}")
    try:
        os.startfile(folder)
    except:
        subprocess.Popen(['xdg-open', folder])
        

timer = QTimer()
def onProjectStart():
    _project.changeTo("on")
    logger.debug(f"当前项目状态：{_project}")
    logger.debug("启动完成")

def onProjectStop():
    _project.changeTo("off")
    logger.debug(f"当前项目状态：{_project}")
    logger.debug("终止完成")


@logger.catch
def switchProject():
    if _project.isRunning():
        logger.info("终止项目！")
        logger.debug("假终止模式，三秒后结束")
        timer.singleShot(3000, onProjectStop)
    else:
        logger.info("启动项目！")
        logger.debug("假启动模式，三秒后结束")
        _project.changeTo("starting")
        timer.singleShot(3000, onProjectStart)