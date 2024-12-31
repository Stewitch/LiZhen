from PySide6.QtCore import QObject, Signal

from .color import ansi_to_html

import sys



class Stream(QObject):
    
    newText = Signal(str)

    def write(self, text: str):
        self.newText.emit(ansi_to_html(str(text)))

    def flush(self):
        pass




_stdout = Stream()
_stderr = Stream()

sys.stdout = _stdout
sys.stderr = _stderr


# _stdout = sys.stdout
# _stderr = sys.stderr