from .logger import logger

import os, subprocess


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