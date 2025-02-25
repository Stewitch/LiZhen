from PySide6.QtCore import QObject, Signal, QProcess
from qfluentwidgets import MessageBox
from signal import SIGTERM, CTRL_C_EVENT
from threading import Thread

from .log import logger, SYSTEM
from .paths import PROJECT, VENV, VENV_ACTIVATE, UV_CONFIG
from .color import ansi_to_html
from .configs import cfg
from .bridge import host, port
from .announce import broad
from .enums import Signals

import os, subprocess, shutil, tomlkit, re, chardet, winshell, webbrowser

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
    with os.popen(commands[SYSTEM]) as r:
        try:
            if SYSTEM == "Windows":
                oid = int(r.read().strip().split(" ")[-1])
            else:
                oid = int(r.read().split("\n")[1].split("  ")[1])
        except:
            pass
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
    """检查系统是否安装了 UV 虚拟环境管理工具"""
    uvPath = shutil.which('uv')
    if uvPath:
        logger.info(f"找到 UV 工具: {uvPath}")
        return True
    
    logger.warning("未找到 UV 工具")
    return False


def checkVenv() -> bool:
    """检查项目是否存在虚拟环境"""
    if os.path.exists(VENV):
        logger.info(f"找到虚拟环境：{VENV}")
        return True
    
    logger.warning("未找到虚拟环境")
    return False


def createShortcut():
    from pathlib import Path

    # 获取桌面路径
    desktop = Path(winshell.desktop())
    cwd = Path.cwd()

    # 定义快捷方式的目标路径和名称
    target = str(cwd.joinpath("lizhen.exe").absolute())
    lnk = desktop.joinpath("离真启动器.lnk")
    if lnk.exists():
        logger.warning("快捷方式已存在")
        broad.cast(Signals.showWarnBar, "快捷方式已存在")
        return
    shortcut_name = str(lnk)

    # 创建快捷方式
    with winshell.shortcut(shortcut_name) as link:
        link.working_directory = str(cwd)
        link.path = target
        link.description = "离真 —— Open-LLM-VTuber 项目启动器"
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
            "activate": f"call {VENV_ACTIVATE}",
            "UVShell": "powershell",
            "UVinstall": 'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex";exit'
        },
        "Linux": {
            # 包括 macOS
            "shell": "sh",
            "arg": "-c",
            "activate": f"source {VENV_ACTIVATE}",
            "UVShell": "sh",
            "UVinstall": "curl -fsSL https://astral.sh/uv/install.sh;exit"
        }
    }
    SYS_SPECIFIED_COMMANDS["Darwin"] = SYS_SPECIFIED_COMMANDS["Linux"]
    
    def __init__(self):
        super().__init__()
        self.__uv = checkUV()
        self.__venv = checkVenv() if self.__uv else False
        self.__startable = self.__uv and self.__venv
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
        self.__activate = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["activate"]
        self.__installUV = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["UVinstall"]
        self.__runServer = f"python {str(PROJECT.joinpath("run_server.py"))} {HF_MIRROR}"
        # self.__runProject = f"{self.__activate} && {self.__runServer}"
        self.__installReq = "uv sync"
        self.__insAndRun = f"{self.__activate} && {self.__installReq} && {self.__runServer};exit"
        
        self.__shell = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["shell"]
        self.__arg = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["arg"]
    
        
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
        
        self.__checkProjectReq()
        self.__backend.start(self.__shell, [self.__arg, self.__insAndRun])
        
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
    
    def isStartable(self):
        return self.__startable
    
    
    def installUV(self):
        shell = self.SYS_SPECIFIED_COMMANDS[SYSTEM]["UVShell"]
        self.__backend.start(shell, [self.__installUV])
        self.__backend.finished.connect(self.__uvInstalled)
    
    def __uvInstalled(self):
        self.__uv = checkUV()
        if self.__uv:
            logger.info("UV 安装完成")
            self.setVenv()
        else:
            broad.cast(Signals.showNoticeDialog, self.tr("UV 安装失败"), self.tr("请前往控制台查看详细信息"))
        self.__backend.finished.disconnect(self.__uvInstalled)
    
    
    def setVenv(self):
        if not self.__uv:
            logger.error("UV 未安装，无法创建虚拟环境")
            return
        self.__backend.start(self.__shell, [self.__arg, "uv venv && exit"])
        self.__backend.finished.connect(self.__venvCreated)
    
    def __venvCreated(self):
        self.__venv = checkVenv()
        if self.__venv:
            self.__startable = True
            logger.info("虚拟环境创建完成")
        else:
            broad.cast(Signals.showNoticeDialog, self.tr("虚拟环境安装失败"), self.tr("请前往控制台查看详细信息"))
        self.__backend.finished.disconnect(self.__venvCreated)
        
    def initUV(self):
        if not self.__uv:
            self.installUV()
        elif not self.__venv:
            self.setVenv()
    
    
    def __detectEncoding(self):
        data = self.__backend.readAllStandardError().data()
        if len(data) >= 2000:
            logger.info(f"尝试从长度 {len(data)} 的数据中检测编码数据")
            charData = chardet.detect(data)
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
            link = f"http://{host}:{port}"
            if not webbrowser.open(link):
                w = MessageBox(
                    self.tr("链接打开失败"),
                    self.tr(f"请手动前往: {link}"),
                    self
                )
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
    if project.isStartable():
        logger.info("UV 已安装，可以启动项目")
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

logger.info("常规功能初始化完成")