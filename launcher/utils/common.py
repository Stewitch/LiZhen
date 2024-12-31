from PySide6.QtCore import QObject, Signal, QProcess

from .logger import logger, SYSTEM
from .paths import PROJECT, VENV, VENV_ACTIVATE, UV_CONFIG
from .color import ansi_to_html

import os, subprocess, shutil, tomlkit



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



def checkUV() -> bool:
    """
    检查系统是否安装了 UV 虚拟环境管理工具
    
    Returns:
        bool: UV 是否存在
    """
    uv_path = shutil.which('uv')
    if uv_path is not None:
        logger.info(f"找到 UV 工具: {uv_path}")
        return True
    
    logger.warning("未找到 UV 工具，尝试安装")
    try:
        if SYSTEM == "Windows":
            logger.info("Windows 系统，尝试通过 PowerShell 安装")
            subprocess.Popen(["powershell", "-ExecutionPolicy", "ByPass", "-c", "irm https://astral.sh/uv/install.ps1 | iex"])
        elif SYSTEM == "Linux" or SYSTEM == "Darwin":
            logger.info("Linux 系统，尝试通过 Shell 安装")
            subprocess.Popen(["sh", "-c", "$(curl -fsSL https://astral.sh/uv/install.sh)"])
        else:
            logger.error(f"未知系统：{SYSTEM}")
            return False
    except:
        logger.error("安装失败")
        return False
    
    return checkUV()


def checkVenv() -> bool:
    """
    检查项目是否存在虚拟环境
    
    Returns:
        bool: 虚拟环境是否存在
    """
    if os.path.exists(VENV):
        logger.info(f"找到虚拟环境：{VENV}")
        return True
    logger.warning("未找到虚拟环境, 尝试创建")
    try:
        subprocess.Popen(["uv", "venv"], cwd=PROJECT)
    except:
        logger.error("创建失败")
        return False
    
    return checkVenv()



class Project(Status):
    
    shellNewText = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.__uv = checkUV()
        self.__venv = checkVenv() if self.__uv else False
        self.__process = QProcess()
        
        self.__initProcess()
        self.__initCommands()
    
    
    def __initProcess(self):
        self.__process.setWorkingDirectory(str(PROJECT))
        self.__process.readyReadStandardError.connect(self.__newText)
        self.__process.finished.connect(lambda: self.changeTo("off"))
        self.__process.started.connect(lambda: self.changeTo("on"))
        
        
    def __initCommands(self):
        if not self.__venv:
            logger.critical("虚拟环境未准备好，无法启动项目")
            return

        if SYSTEM == "Windows":
            self.__activate = f"call {VENV_ACTIVATE}"
        else:
            self.__activate = f"source {VENV_ACTIVATE}"
        self.__runProject = f"{self.__activate} && python {str(PROJECT.joinpath("run_server.py"))}"
    
    
    def start(self):
        if self.__process.state() == QProcess.Running:
            logger.warning("项目已经在运行")
            return
        
        if SYSTEM == "Windows":
            self.__process.start("cmd", ["/k", self.__runProject])
        else:  # Linux or MacOS
            self.__process.start("sh", ["-c", self.__runProject])
        
        self.changeTo("starting")
        
    
    def stop(self):
        self.__process.kill()
    
    
    def uvAvailable(self):
        return self.__uv
    
    
    def venvAvailable(self):
        return self.__venv
    
    
    def __newText(self):
        msg = self.__process.readAllStandardError().data().decode(errors="replace")
        html_msg = ansi_to_html(msg)
        self.shellNewText.emit(html_msg)
        logger.debug("项目进程新消息")
        logger.info(html_msg)



project = Project()



def openFolder(folder: str):
    if not isinstance(folder, str):
        logger.error(f"文件夹路径错误：{folder}")
        return
    logger.debug(f"打开文件夹：{folder}")
    try:
        os.startfile(folder)
    except:
        subprocess.Popen(['xdg-open', folder])



def onProjectStart():
    logger.debug(project.uvAvailable())
    if project.uvAvailable():
        logger.info("UV 已安装，启动项目")
        project.start()
    logger.debug(f"当前项目状态：{project}")
    logger.debug("启动完成")

def onProjectStop():
    project.stop()
    logger.debug(f"当前项目状态：{project}")
    logger.debug("终止完成")


@logger.catch
def switchProjectState():
    if project.isRunning():
        logger.info("终止项目！")
        onProjectStop()
    else:
        logger.info("启动项目！")
        project.changeTo("starting")
        onProjectStart()



def pipMirrorFile(enable: True):
    if enable:
        pipMirror = {'index': [{'url': 'https://pypi.tuna.tsinghua.edu.cn/simple'}]}
        with open(UV_CONFIG, "w") as f:
            tomlkit.dump(pipMirror, f)
        logger.info("启用 pip 镜像")
    else:
        if os.path.exists(UV_CONFIG):
            os.remove(UV_CONFIG)
            logger.info("关闭 pip 镜像")