from .Interfaces import ManagerInterface



class TTSInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "TTS 管理"):
        super().__init__(parent, title, True)