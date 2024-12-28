from PySide6.QtCore import QObject, Signal

import sys



class Stream(QObject):
    
    newText = Signal(str)

    def write(self, text: str):
        self.newText.emit(str(text))

    def flush(self):
        pass



_stdout = Stream()
_stderr = Stream()

sys.stdout = _stdout
sys.stderr = _stderr