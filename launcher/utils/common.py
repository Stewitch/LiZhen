from PySide6.QtCore import QObject, Signal, QProcess
from signal import SIGTERM, CTRL_C_EVENT
from threading import Thread

from .log import logger, SYSTEM
from .paths import PROJECT, VENV, VENV_ACTIVATE, UV_CONFIG
from .color import ansi_to_html

import os, subprocess, shutil, tomlkit, re, chardet



VERSION = "0.3.6"

SIGEND = CTRL_C_EVENT if SYSTEM == "Windows" else SIGTERM



commands = {"Windows": 'netstat -aon|findstr "12393"', "Linux": 'lsof -i tcp:12393'}

def getPortOccupantPid() -> int | None:
    oid = None
    def worker():
        nonlocal oid
        with os.popen(commands[SYSTEM]) as r:
            try:
                if SYSTEM == "Windows":
                    oid = int(r.read().strip().split(" ")[-1])
                else:
                    oid = int(r.read().split("\n")[1].split("  ")[1])
            except:
                pass
    wt = Thread(target=worker)
    wt.start()
    wt.join()
    if oid is None:
        logger.info("未找到可能占用12393端口的进程")
    return oid

occupantPid = getPortOccupantPid()
if occupantPid is not None:
    try:
        os.kill(occupantPid, SIGEND)
        logger.info(f"终止占用端口的进程：{occupantPid}")
    except Exception as e:
        logger.error(f"尝试终止占用端口的进程失败，原因： {e}")



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
    tryToStop = Signal()
    SYS_SPECIFIED_COMMANDS = {
        "Windows": {
            "shell": "cmd",
            "arg": "/k",
            "activate": f"call {VENV_ACTIVATE}"
        },
        "Linux": {
            # 包括 macOS
            "shell": "sh",
            "arg": "-c",
            "activate": f"source {VENV_ACTIVATE}"
        }
    }
    
    def __init__(self):
        super().__init__()
        self.__uv = checkUV()
        self.__venv = checkVenv() if self.__uv else False
        self.__backend = QProcess()
        self.__serverPid = None
        self.__encoding = "gbk"
        
        self.__initBackend()
        self.__initCommands()

    
    def __initBackend(self):
        self.__backend.setWorkingDirectory(str(PROJECT))
        self.__backend.readyReadStandardError.connect(self.__detectEncoding)
        self.__backend.readyReadStandardError.connect(self.__newStderr)
        self.__backend.readyReadStandardOutput.connect(self.__newStdout)
        
        
    def __initCommands(self):
        if not self.__venv:
            logger.critical("虚拟环境未准备好，无法启动项目")
            return

        self.__activate = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["activate"]
            
        self.__runServer = f"python {str(PROJECT.joinpath("run_server.py"))}"
        self.__runProject = f"{self.__activate} && {self.__runServer}"
        self.__installReq = "uv pip install --requirements pyproject.toml"
        self.__insAndRun = f"{self.__activate} && {self.__installReq} && {self.__runServer}"
        
    
    def __checkProjectReq(self):
        if not self.__venv:
            logger.critical("虚拟环境不存在，无法检测项目依赖")
            return
        
        shell = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["shell"]
        proc = subprocess.Popen(
            [f'{shell}'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=PROJECT)
        
        req = None
        out, _ = proc.communicate(input=b'uv pip list --format json\n')
        for l in out.decode(errors="ignore").split():
            if l.startswith("[") and l.endswith("]"):
                req = l
        
        if len(req) <= 22:
            return False
        return True
                
        
    def start(self):
        if self.__backend.state() == QProcess.Running:
            logger.warning("项目启动中，强制终止可能会导致一些问题")
            return
        
        shell = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["shell"]
        arg = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["arg"]
        
        if self.__checkProjectReq():
            self.__backend.start(shell, [arg, self.__runProject])
        else:
            self.__backend.start(shell, [arg, self.__insAndRun])
        
        self.changeTo("starting")
        self.shellNewText.connect(self.__stateUpdateByText)
    
    def __killServer(self):
        try:
            os.kill(self.__serverPid, SIGEND)
        except:
            logger.warning("终止服务器进程失败，可能是因为服务器未启动")
        
    
    def stop(self):
        self._forceStop()
        self.changeTo("off")
    
    def _forceStop(self):
        self.__killServer()
        self.__backend.kill()
    
    
    def uvAvailable(self):
        return self.__uv
    
    
    def venvAvailable(self):
        return self.__venv
    
    
    def __detectEncoding(self):
        data = self.__backend.readAllStandardError().data()
        if len(data) >= 800:
            charData = chardet.detect(data)
            logger.info(f"尝试从长度 {len(data)} 的数据中检测编码数据")
            logger.info(f"结果：{charData}")
            if charData["encoding"] is not None and charData["confidence"] > 0.85:
                self.__encoding = charData["encoding"]
                self.__backend.readyReadStandardError.disconnect(self.__detectEncoding)
        self.__newText(data.decode(self.__encoding, "replace"))
    
    
    def __newText(self, text: str):
        html_msg = ansi_to_html(text)
        self.shellNewText.emit(html_msg)
    
    def __newStderr(self):
        msg = self.__backend.readAllStandardError().data().decode(
            self.__encoding, "replace")
        self.__newText(msg)
    
    def __newStdout(self):
        msg = self.__backend.readAllStandardOutput().data().decode(
            self.__encoding, "replace")
        self.__newText(msg)
        
    
    def __stateUpdateByText(self, text: str):
        if "Started server process" in text:
            logger.debug("触发服务器PID获取")
            if match := re.search(r'\[(\d+)\]', text):
                self.__serverPid = int(match.group(1))
            logger.debug(f"服务器PID：{self.__serverPid}")
            
        if "Application startup complete." in text:
            self.changeTo("on")
            logger.info("项目启动完成")
            self.shellNewText.disconnect(self.__stateUpdateByText)
        


project = Project()



def openFolder(folder: str):
    if not isinstance(folder, str):
        logger.error(f"文件夹路径错误：{folder}")
        return
    logger.debug(f"打开文件夹：{folder}")
    if SYSTEM == "Windows":
        os.startfile(folder)
        return
    try: # MacOS
        subprocess.Popen(['open', folder])
    except: # Linux
        subprocess.Popen(['xdg-open', folder])



def onProjectStart():
    logger.debug(project.uvAvailable())
    if project.uvAvailable():
        logger.info("UV 已安装，启动项目")
        project.start()
    logger.debug(f"当前项目状态：{project}")
    logger.info("项目启动中")
    

def onProjectStop():
    project.stop()
    logger.debug(f"当前项目状态：{project}")
    logger.debug("项目终止完成")


@logger.catch
def switchProjectState():
    if project.isRunning() is None:
        project.tryToStop.emit()
    elif project.isRunning():
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