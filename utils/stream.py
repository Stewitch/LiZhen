from PySide6.QtCore import QObject, Signal, QThread
from enum import Enum

import re, queue, sys



# 预编译正则表达式，合并\x1b和\033的情况
ANSI_ESCAPE_PATTERN = re.compile(r'\x1b\[([0-9;]+)m')

ANSI_COLOR_MAP = {
    # 前景色 (仅使用的颜色)
    '34': 'color: #1E90FF',  # Debug
    '33': 'color: #F1BB00',  # Warning
    '31': 'color: #FF0000',  # Error
    '32': 'color: #32CD32',  # <green></green>
    '36': 'color: #008B8B',  # <cyan></cyan>
    
    # 背景色 (仅使用的颜色)
    '41': 'background-color: #FF5555',  # Critical
    
    # 文本样式 (仅使用的样式)
    '0': '',  # 重置
    '1': 'font-weight: bold',  # 粗体
    '3': 'font-style: italic',  # 斜体
    '4': 'text-decoration: underline',  # 下划线
    '9': 'text-decoration: line-through',  # 删除线
}



def ANSIToHtml(text: str) -> str:
    isProgress = ('Downloading' in text or 'sherpa-onnx' in text) and '%' in text
    if isProgress:
        text = text.rstrip() + '\r'

    openedSpans = [0]

    def replaceCodes(match):
        codes = match.group(1).split(';')
        styles = []

        if '0' in codes:
            html = '</span>' * openedSpans[0]
            openedSpans[0] = 0
            return html

        for code in codes:
            if code in ANSI_COLOR_MAP:
                styles.append(ANSI_COLOR_MAP[code])

        if not styles:
            if openedSpans[0] > 0:
                openedSpans[0] -= 1
                return '</span>'
            return ''

        openedSpans[0] += 1
        return f'<span style="{"; ".join(styles)}">'

    result = ANSI_ESCAPE_PATTERN.sub(replaceCodes, text)
    if openedSpans[0] > 0:
        result += '</span>' * openedSpans[0]

    return result



class StandardStream(Enum):
    
    """标准流枚举
    
    用于保留标准输出和标准错误流的引用
    """
    
    STDOUT = sys.stdout
    STDERR = sys.stderr



class QueuedStream:
    
    """队列流
    用于将标准输出和标准错误重定向到队列中，便于在 Qt 线程中处理
    
    使用方法:
    ```python
    sys.stdout = QueuedStream(StandardStream.STDOUT)
    ```
    建议使用 `QMsgThread` 类来处理队列中的消息
    """
    
    def __init__(self, stdStream: StandardStream):
        self.stdStream = stdStream
        self.queue = queue.Queue()
        self.flush = self.stdStream.value.flush
        
    def write(self, text: str):
        self.queue.put(text)
    
    def close(self):
        if self.stdStream is StandardStream.STDOUT:
            sys.stdout = self.stdStream.value
        elif self.stdStream is StandardStream.STDERR:
            sys.stderr = self.stdStream.value
        self.queue.put("__TERM__")



class Receiver(QObject):
    
    newText = Signal(str)
    
    def __init__(self, stream: QueuedStream):
        super().__init__()
        self.stream = stream
    
    def listen(self):
        while True:
            try:
                text = self.stream.queue.get()
                if "__TERM__" in text:
                    break
                self.newText.emit(ANSIToHtml(text))
            except queue.Empty:
                continue
    


class QMsgThread(QThread):
    
    """消息线程
    用于将标准输出和标准错误重定向到 Qt 线程中
    
    使用方法:
    ```python
    sys.stdout = QueuedStream(StandardStream.STDOUT)
    msgThread = QMsgThread.fromQueueStream(sys.stdout)
    msgThread.bind(textEdit.append)
    msgThread.start()
    ```
    关闭方法:
    ```python
    msgThread.quit()
    msgThread.wait() # 等待线程结束
    ```
    """
    
    def __init__(self, receiver: Receiver):
        """请使用 `QMsgThread.fromQueuedStream()` 构造方法"""
        super().__init__()
        self.receiver = receiver
        self.receiver.moveToThread(self)
        self.started.connect(self.receiver.listen)
    
    def quit(self) -> None:
        if self.isRunning() and self.receiver:
            self.receiver.stream.close()
        return super().quit()
    
    @classmethod
    def fromQueuedStream(cls, stream: QueuedStream) -> 'QMsgThread':
        receiver = Receiver(stream)
        return cls(receiver)
    
    def bind(self, func) -> None:
        self.receiver.newText.connect(func)



# 全局替换标准错误(loguru默认使用sys.stderr)
stderr_ = QueuedStream(StandardStream.STDERR)
stderrReceiver = Receiver(stderr_)
sys.stderr = stderr_



# 测试
if __name__ == "__main__":
    
    from PySide6.QtWidgets import QApplication, QTextEdit
    
    app = QApplication(sys.argv)
    textEdit = QTextEdit()
    textEdit.resize(160, 200)
    textEdit.setReadOnly(True)
    
    # 替换标准输出
    sys.stdout = QueuedStream(StandardStream.STDOUT)
    msgThread = QMsgThread.fromQueuedStream(sys.stdout)
    msgThread.bind(textEdit.append)
    msgThread.start()
    textEdit.setStyleSheet("""
    QTextEdit {
        white-space: pre-wrap;
    }
    """)
    
    textEdit.show()
    
    # 重定向 stdout 和 ANSI 样式转换测试
    print('\033[1;30mH\033[1;31me\033[1;32ml\033[1;33ml\033[1;36mo, \033[1;41m\033[1;34mWorld!\033[0m')
    print('\033[0mHello World!')
    print('\033[1mHello World!')
    print('\033[3mHello World!')
    print('\033[4mHello World!')
    print('\033[9mHello World!')
    
    # 等待线程结束
    msgThread.quit()
    msgThread.wait()
    
    # 恢复原始输出
    print('End of QueueStream Test')
    sys.exit(app.exec())