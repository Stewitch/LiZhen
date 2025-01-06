from .Interfaces import ManagerInterface



class ASRInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "ASR 管理"):
        super().__init__(parent, title, True)