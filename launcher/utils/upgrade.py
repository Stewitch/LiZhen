from PySide6.QtCore import QObject, Signal
from pathlib import Path

from .log import logger

from ..interfaces.Widgets import RestartDialog

import subprocess



class Updater(QObject):
    
    showError = Signal(str)
    terminate = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.repo = None
        self.executable = "updater.exe"
        self.args = ["-r", self.repo]
    
    
    def setRepo(self, repo: str):
        self.repo = repo.lower()
        if self.executable == "python":
            self.args = ["updater.py", "-r", self.repo]
            return
        self.args = ["-r", self.repo]
    
    
    def setExecutable(self, file: str | Path):
        if not isinstance(file, (Path, str)):
            logger.error(f"文件路径错误: {file}")
            return
        file = Path(file)
        if file.is_file() and file.suffix == ".exe" and file.exists():
            self.executable = str(file)
        else:
            logger.error(f"文件不存在或不是可执行文件: {file}")
    
    
    def setPythonRuntime(self):
        self.executable = "python"
        self.args = ["updater.py", "-r", self.repo]
            
    
    def exec(self):
        logger.info(f"更新程序: {self.executable} {self.args}")
        if self.repo not in ["gitee", "github"]:
            self.showError.emit(self.tr(f"未知的更新仓库: {self.repo}"))
            return
        try:
            w = RestartDialog(
                self.tr("关闭通知"),
                self.tr("运行更新程序需要关闭启动器，是否继续？\n更新完成后启动器将自动重启"),
                self.parent()
            )
            w.yesButton.setText(self.tr("继续"))
            w.cancelButton.setText(self.tr("取消"))
            if w.exec():
                subprocess.Popen([self.executable, *self.args])
                self.terminate.emit()
            else:
                return
            
        except Exception as e:
            logger.error(f"启动更新程序失败：{e}")
            self.showError.emit(self.tr(f"启动更新程序失败"))


logger.info('更新器初始化完成')