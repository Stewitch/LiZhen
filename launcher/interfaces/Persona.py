from .Interfaces import ManagerInterface



class PersonaInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "人格提示词"):
        super().__init__(parent, title)