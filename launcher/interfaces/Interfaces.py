from qfluentwidgets import ScrollArea



class SubInterface:
    pass



class ManagerInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        