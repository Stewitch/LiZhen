from PySide6.QtCore import QProcess, QObject, Signal
from pathlib import Path

from .log import logger



class Updater(QObject):
    
    updateFinished = Signal()
    showError = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.repo = None
        self.executable = "updater.exe"
        self.process = QProcess()
        self.args = ["-r", self.repo]
        
        self.process.finished.connect(lambda: self.updateFinished.emit())
    
    
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
        if self.process.state() is QProcess.ProcessState.Running:
            self.showError.emit(self.tr("更新程序正在运行！"))
            return
        elif self.repo not in ["gitee", "github"]:
            self.showError.emit(self.tr(f"未知的更新仓库: {self.repo}"))
            return
        self.process.start(self.executable, self.args)


logger.info('更新器初始化完成')