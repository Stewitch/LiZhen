from .Interfaces import ManagerInterface



class LLMInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "LLM 管理"):
        super().__init__(parent, title, True)