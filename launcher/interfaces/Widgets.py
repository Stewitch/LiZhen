from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QFont
from qfluentwidgets import ElevatedCardWidget, ImageLabel, CaptionLabel, ImageLabel, BodyLabel

from ..utils.configs import cfg
from ..utils.logger import logger



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
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        
        self.title.setFont(font)
        
        font.setPointSize(10)
        self.provider.setFont(font)
        
        font.setPointSize(8)
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
        img = f"./launcher/assets/images/ui/{theme}/{self.imgName}"
        self.icon.setImage(img)
        self.icon.setFixedSize(QSize(90,90))
        logger.debug(f"更新图标：{self.imgName}, 主题：{theme}")

 
 