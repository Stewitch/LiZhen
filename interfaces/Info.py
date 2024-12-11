from interfaces.ui.Ui_Info import Ui_Info
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

class InfoInterface(QWidget, Ui_Info):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.infoHeaderImg.setImage("./launcher/assets/images/infoHeader.png")
        self.toGithub.setIcon(FluentIcon.GITHUB)
        self.toGithub.setUrl("https://github.com/SunKSugaR/LiZhen")
        self.toLicense.setIcon(FluentIcon.DICTIONARY)
        self.toLicense.setUrl("https://www.gnu.org/licenses/gpl-3.0.html")
        