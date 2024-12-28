from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QFont
from qfluentwidgets import ElevatedCardWidget, ImageLabel, CaptionLabel, ImageLabel, BodyLabel

from ..utils.configs import cfg
from ..utils.logger import logger
from ..utils.paths import UICONS

import os.path



class ModelDisplayCard(ElevatedCardWidget):

    def __init__(self, parent=None, iconPath: str = "test", name: str = "test"):
        super().__init__(parent)
        self.icon = ImageLabel(iconPath, self)
        self.title = CaptionLabel(name, self)
        self.provider = BodyLabel("测试", self)
        self.model = BodyLabel("模型",self)
        self.imgName = None

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.icon, 0, Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.title, 0, Qt.AlignHCenter | Qt.AlignBottom)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.provider, 0, Qt.AlignHCenter | Qt.AlignBottom)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.model, 0, Qt.AlignHCenter | Qt.AlignBottom)

        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(13)
        font.setBold(True)
        
        self.title.setFont(font)
        
        font.setPointSize(12)
        self.provider.setFont(font)
        
        font.setItalic(True)
        font.setPointSize(10)
        self.model.setFont(font)
        
        
        # self.resize(200, 180)
        # self.setMinimumHeight(150)
        
        cfg.themeChanged.connect(self.updateIcon)
    
    def setIcon(self, name: str):
        """图标必须放在./launcher/assets/images/ui/{theme}/文件夹下"""
        self.imgName = name
        self.updateIcon()
        
    
    def updateIcon(self):
        theme = cfg.theme.value.lower()
        img = str(UICONS.joinpath(f"{theme}/{self.imgName}"))
        self.icon.setImage(img)
        self.icon.setFixedSize(QSize(90,90))
        if self.imgName is None or not os.path.exists(img):
            logger.warning(f"图标不存在：{img}")
        else:
            logger.debug(f"更新图标：{self.imgName}, 主题：{theme}")
    
    def _init(self, iconName: str, name: str, provider: str, model: str):
        """图标必须放在./launcher/assets/images/ui/{theme}/文件夹下"""
        logger.info(f"初始化模型卡片：{name.strip(":")}")
        self.setIcon(iconName)
        self.title.setText(name)
        self.provider.setText(provider)
        self.model.setText(model)

 
 