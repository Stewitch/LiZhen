from .Interfaces import ManagerInterface



class CharacterInterface(ManagerInterface):
    
    def __init__(self, parent=None, title = "角色设定"):
        super().__init__(parent, title, True)