from .logger import logger

import os, subprocess


def openFolder(folder: str):
    logger.debug(f"打开文件夹：{folder}")
    try:
        os.startfile(folder)
    except:
        subprocess.Popen(['xdg-open', folder])



def startProject():
    logger.info("启动项目！")