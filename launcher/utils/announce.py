from PySide6.QtCore import Signal, QObject

from .enums import Signals
from .log import logger



class Announcer(QObject):
    
    showErrBar = Signal(str)
    showNoticeDialog = Signal(str)
    showWarnBar = Signal(str)
    showInfoBar = Signal(str)
    changeProjectFolder = Signal(str)
    agentUpdate = Signal(str)
    llmProviderUpdate = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.signalDict = {
            0: self.showInfoBar,
            1: self.showWarnBar,
            2: self.showErrBar,
            3: self.showNoticeDialog,
            99: self.changeProjectFolder,
            1000: self.agentUpdate,
            1001: self.llmProviderUpdate,
        }
    
    
    @logger.catch
    def cast(self, sig: Signals, *args):
        self.signalDict[sig.value].emit(*args)
        


broad = Announcer()