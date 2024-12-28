from PySide6.QtGui import QColor
from PySide6.QtCore import QObject, Signal

from .logger import logger

import os, subprocess



class Status(QObject):
    
    changed = Signal(bool)

    def __init__(self, status: bool = False):
        super().__init__()
        self.__status = status
        
    
    def isRunning(self) -> bool:
        if self.__status:
            return True
        return False
    
    
    def changeTo(self, s: bool):
        if isinstance(s, bool):
            self.__status = s
            self.changed.emit(s)
    
    
    def switch(self):
        self.__status = not self.__status
        self.changed.emit(self.__status)



_project = Status()
_launcher = Status()



class Color:
    RED = QColor(255, 0, 0)
    GREEN = QColor(0, 255, 0)
    BLUE = QColor(0, 0, 255)



def openFolder(folder: str):
    if not isinstance(folder, str):
        logger.error(f"文件夹路径错误：{folder}")
        return
    logger.debug(f"打开文件夹：{folder}")
    try:
        os.startfile(folder)
    except:
        subprocess.Popen(['xdg-open', folder])


def startProject():
    logger.info("启动项目！")