from PySide6.QtCore import QObject, Signal, QProcess
from signal import SIGTERM, CTRL_C_EVENT
from threading import Thread

from .log import logger, SYSTEM
from .paths import PROJECT, VENV, VENV_ACTIVATE, UV_CONFIG
from .color import ansi_to_html
from .configs import cfg
from .bridge import port
from .announce import broad

import os, subprocess, shutil, tomlkit, re, chardet

FASTERINIT = 0


SIGEND = CTRL_C_EVENT if SYSTEM == "Windows" else SIGTERM

if cfg.get(cfg.hfMirrorEnabled):
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    HF_MIRROR = "--hf_mirror"
else:
    HF_MIRROR = ""



commands = {"Windows": f'netstat -aon|findstr "{port}"', "Linux": f'lsof -i tcp:{port}'}

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
        logger.info(f"未找到可能占用{port}端口的进程")
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


def createShortcut():
    import winshell
    from pathlib import Path

    # 获取桌面路径
    desktop = Path(winshell.desktop())

    # 定义快捷方式的目标路径和名称
    target = r"C:\Path\To\Your\Application.exe"
    shortcut_name = desktop / "离真启动器.lnk"

    # 创建快捷方式
    with winshell.shortcut(shortcut_name) as link:
        link.path = target
        link.description = "离真启动器 for Open-LLM-VTuber Project."
        link.icon_location = (target, 0)


extraCommands = []

def extraCommand(command):
    global extraCommands
    if command not in extraCommands:
        extraCommands.append(command)
        logger.info(f"已添加额外命令 {command}")

broad.extraCommand.connect(extraCommand)



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
        
        self.__runServer = f"python {str(PROJECT.joinpath("run_server.py"))} {HF_MIRROR}"
        # self.__runProject = f"{self.__activate} && {self.__runServer}"
        self.__installReq = "uv sync"
        self.__insAndRun = f"{self.__activate} && {self.__installReq} && {self.__runServer}"
        
    @logger.catch
    def __checkProjectReq(self):
        for cmd in extraCommands:
            self.__installReq += f" && {cmd}"
        self.__insAndRun = f"{self.__activate} && {self.__installReq} && {self.__runServer}"
        logger.debug(f"项目启动命令：{self.__insAndRun}")
        extraCommands.clear()
        
        
    def start(self):
        if self.__backend.state() == QProcess.Running:
            logger.warning("项目启动中，强制终止可能会导致一些问题")
            return
        
        shell = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["shell"]
        arg = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["arg"]
        
        self.__checkProjectReq()
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
            self.__encoding, "replace"
        )
        self.__newText(msg)
    
    def __newStdout(self):
        msg = self.__backend.readAllStandardOutput().data().decode(
            self.__encoding, "replace"
        )
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
    
pipMirrorFile(cfg.get(cfg.pipMirrorEnabled))