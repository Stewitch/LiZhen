from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui.Ui_Info import Ui_Info

from ..utils.paths import IMAGES



class InfoInterface(QWidget, Ui_Info):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.infoHeaderImg.setImage(IMAGES.joinpath("infoHeader.png"))
        self.toGithub.setIcon(FluentIcon.GITHUB)
        self.toGithub.setUrl("https://github.com/SunKSugaR/LiZhen")
        self.toLicense.setIcon(FluentIcon.DICTIONARY)
        self.toLicense.setUrl("https://www.gnu.org/licenses/gpl-3.0.html")
        