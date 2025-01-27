from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QLabel,
                               QProgressBar, QApplication, QGridLayout)
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtCore import Qt, Signal
from typing import Dict
from pathlib import Path

import argparse, shutil, json, requests, threading, sys



def load_config(path: str | Path):
    if not isinstance(path, (str, Path)):
        return
    
    
    path = Path(path)
    if path.is_file():
        with open(path, 'r', encoding='utf-8') as f:
            cfg: dict = json.load(f)
            return cfg
    else:
        return


def parse_args():
    parser = argparse.ArgumentParser(description="离真启动器 更新器")
    parser.add_argument("-d", "--debug", action="store_true", help="启用调试模式")
    parser.add_argument("-c", "--config", type=Path, help="指定配置文件路径")
    parser.add_argument("-r", "--repo", type=str, help="指定下载仓库(gh: GitHub / ge: Gitee), 默认 gh")
    parser.add_argument("-tp", "--temp_path", type=Path, help="指定临时下载路径(默认为当前目录下的 temp 文件夹)")
    parser.add_argument("-cs", "--chunk_size", type=int, help="块大小(单位 MB), 默认 100")
    parser.add_argument("-lr", "--launcher_running", action="store_true", help="启动器正在运行(将结束启动器进行更新)")
    return parser.parse_args()



class Updater(QWidget):
    
    updateProgress = Signal(int)
    downloadCompleted = Signal(Path)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }

    
    def __init__(self,
                 config: Dict[str, dict],
                 debug=None, repo=None, 
                 chunkSize=None, tempPath=None):
        super().__init__(parent=None)
        self.__config = config.get("updater", None)
        if not self.__config:
            raise ValueError("配置文件中没有找到更新器配置")
        self.debug = debug if debug is not None else self.__config.get("debug", False)
        self.tempPath = tempPath if tempPath else Path(self.__config.get("tempPath", Path("temp")))
        self.maxChunkSize = chunkSize if chunkSize else self.__config.get("maxChunkSize", 100) * 1024 * 1024
        self.repo = repo if repo else self.__config.get("url", {}).get(
            "GitHub", "https://api.github.com/repos/SunKSugaR/LiZhen/releases/latest"
        )
        
        self.repo_ = "gh" if "github" in self.repo else "ge"
        self.cfg = config
        
        self.version = config.get("version", None)
        self.updateInfo = {}
        self.downloadedFile = None
        
        self.__initUI()
        self.__SSConnections()
        self.__initData()
    

        if self.debug:
            self.__enableDebug()
        else:
            self.execAll()
            
    
    def __initUI(self):
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.vBoxLayout.setSpacing(5)
        self.vBoxLayout.setContentsMargins(15, 5, 5, 15)
        
        titleFont = QFont()
        titleFont.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        titleFont.setPointSize(18)
        self.title = QLabel(self.tr("启动器更新"), self)
        self.title.setFont(titleFont)
        self.vBoxLayout.addWidget(self.title, 1, Qt.AlignmentFlag.AlignLeft)
        
        self.mainWidget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setContentsMargins(35, 5, 35, 20)
        
        progressFont = QFont()
        progressFont.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        progressFont.setPointSize(13)
        self.progress = QLabel(self.tr("等待中"), self)
        self.progress.setFont(progressFont)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimumWidth(430)
        self.progressBar.setRange(0, 4)
        self.mainLayout.addWidget(self.progress, 1, Qt.AlignmentFlag.AlignLeft)
        self.mainLayout.addWidget(self.progressBar, 2, Qt.AlignmentFlag.AlignCenter)
        
        self.vBoxLayout.addWidget(self.mainWidget, 2, Qt.AlignmentFlag.AlignCenter)
        self.resize(480, 250)
        
        with open(Path("./launcher/assets/qss/Updater.qss"), "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())
        
        self.setWindowIcon(QIcon("./launcher/assets/images/LZ64.ico"))
        self.setWindowTitle(self.tr("启动器更新"))
    
    def __initData(self):
        if not self.tempPath.exists():
            self.tempPath.mkdir()
            
    
    def checkUpdate(self):
        self.progressBar.setValue(0)
        print(self.repo)
        print("-"*50)
        try:
            response = requests.get(self.repo, headers=self.headers)
        except requests.exceptions.SSLError:
            self.progress.setText(self.tr("SSL 认证失败，请尝试打开代理"))
        if response.status_code != 200:
            print(f"检查更新失败: {response.status_code}")
            self.progress.setText(self.tr(f"检查更新失败: {response.status_code}, 请尝试更换仓库"))
            return
        data = response.json()
        print(data)
        latestVersion = data.get("tag_name", None)
        
        if latestVersion == self.cfg.get("version"):
            self.progress.setText(self.tr("已是最新版本"))
            self.progressBar.setValue(4)
            return True
        
        releaseID = data.get("id")
        downloadUrl = data.get("assets")[0]["browser_download_url"]
        fileName = downloadUrl.split("/")[-1]
        fileSize = data.get("assets")[0].get("size", 0)
        print("-"*50)
        if self.repo_ == "ge":
            response = requests.get(self.cfg.get("url").get("geSize").format(rid=releaseID), headers=self.headers)
            if response.status_code != 200:
                print(f"获取release文件大小失败: {response.status_code}")
                fileSize = 0
            data = response.json()
            print(data)
            fileSize = data[0].get("size", 0)
        
        self.progress.setText(self.tr(f"当前版本: {self.version}\n最新版本: {latestVersion}\n文件名: {fileName}\n文件大小: {fileSize}"))
        self.updateInfo["releaseID"] = releaseID
        self.updateInfo["latestVersion"] = latestVersion
        self.updateInfo["downloadUrl"] = downloadUrl
        self.updateInfo["fileName"] = fileName
        self.updateInfo["fileSize"] = fileSize
        self.cfg["lastUpdateInfo"] = self.updateInfo
        
        self.progressBar.setValue(1)
        
    
    def downloadUpdate(self):
        def worker():
            response = requests.get(self.updateInfo["downloadUrl"], stream=True)
            if response.status_code != 200:
                print(f"下载更新失败: {response.status_code}")
                self.progress.setText(self.tr("下载更新失败"))
                return
            file = self.tempPath.joinpath(self.updateInfo.get("fileName")).absolute()
            if not file.exists():
                file.touch()
            with open(file, "wb") as f:
                for chunk in response.iter_content(chunk_size=self.maxChunkSize):
                    if chunk:
                        f.write(chunk)
                        self.updateProgress.emit(len(chunk))
            self.downloadCompleted.emit(file)
        downloadThread = threading.Thread(target=worker)
        self.progressBar.setRange(0, self.updateInfo["fileSize"])
        self.progress.setText(self.tr("下载中..."))
        downloadThread.start()
        
    
    def extractFiles(self):
        pass
    
    
    def removeTempFiles(self):
        shutil.rmtree(self.tempPath)
        self.progress.setText(self.tr("已删除临时文件"))
        self.progressBar.setValue(4)


    def execAll(self):
        pass
    
    
    def __updateProgress(self, v: int):
        self.progressBar.setValue(v)
        
    def __onDownloadCompleted(self, file):
        self.downloadedFile = file
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, 4)
        self.progressBar.setValue(2)
        if not self.debug:
            self.extractFiles()
    
    def __SSConnections(self):
        self.updateProgress.connect(self.__updateProgress)
        self.downloadCompleted.connect(self.__onDownloadCompleted)
    
    def __enableDebug(self):
        self.debugWidget = QWidget(self)
        self.gridLayout = QGridLayout(self.debugWidget)
        
        buttonFont = QFont()
        buttonFont.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        buttonFont.setPointSize(11)
        self.checkUpdateButton = QPushButton(
            self.tr("检查更新"),    
            self
        )
        self.downloadUpdateButton = QPushButton(
            self.tr("下载更新"),
            self
        )
        self.removeButton = QPushButton(
            self.tr("删除临时文件"),
            self
        )
        self.downloadUpdateButton.setFont(buttonFont)
        self.checkUpdateButton.setFont(buttonFont)
        self.removeButton.setFont(buttonFont)
        
        self.progressBar.setValue(1)
        
        self.gridLayout.addWidget(self.checkUpdateButton)
        self.gridLayout.addWidget(self.downloadUpdateButton)
        self.gridLayout.addWidget(self.removeButton)
        
        self.vBoxLayout.addWidget(self.debugWidget)
        
        self.checkUpdateButton.clicked.connect(self.checkUpdate)
        self.downloadUpdateButton.clicked.connect(self.downloadUpdate)
        self.removeButton.clicked.connect(self.removeTempFiles)
    
    
    def closeEvent(self, event):
        if self.debug:
            event.accept()
            return
        try:
            self.removeTempFiles()
        except:
            pass
        event.accept()


if __name__ == "__main__":
    args = parse_args()
    conf = args.config if args.config else Path("./launcher/configs/updater.json")
    debug = args.debug if args.debug else None
    repo = args.repo if args.repo else "gh"
    tempPath = args.temp_path if args.temp_path else None
    chunkSize = args.chunk_size if args.chunk_size else None
    
    config = load_config(conf)
    repo = config["url"][config["args"]["repo"][repo]]
    if config is None:
        raise FileNotFoundError(f"配置文件不存在: {conf}")
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(str("./launcher/assets/fonts/Alibaba-PuHuiTi-Regular.ttf"))
    updater = Updater(config, debug, repo, chunkSize, tempPath)
    updater.show()
    sys.exit(app.exec())
    