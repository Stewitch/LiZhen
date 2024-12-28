from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtCore import Qt
from qfluentwidgets import Action, FluentIcon

from .ui.Ui_Console import Ui_Console

from ..utils.logger import logger
from ..utils.common import Color, _project
from ..utils.stream import _stdout, _stderr



class ConsoleInterface(QWidget, Ui_Console):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.__initWidgets()
        self.__initFunctions()
        self.__SSConnection()
        
        self.statusUpdate()
        
        
    def __initWidgets(self):
        self.setupUi(self)
        self.setObjectName("ConsoleInterface")
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 R"])
        font.setPointSize(12)
        self.cmdBar.setFont(font)
        
        self.cmdBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.cmdBar.addActions([
            Action(FluentIcon.BROOM, self.tr("清空"), triggered=self.clear),
            Action(FluentIcon.SAVE_AS, self.tr("导出信息"), triggered=self.saveAs),
            Action(FluentIcon.ROTATE, self.tr("启动器控制台"), triggered=self.switchStream)
        ])
    
    
    def __initFunctions(self):
        self.currentShell = self.Shells.currentWidget().children()[1]
        self.stdout = _stdout
        self.stderr = _stderr
    
    def __SSConnection(self):
        _project.changed.connect(self.statusUpdate)
        self.stdout.newText.connect(self.launcherShellUpdate)
        self.stderr.newText.connect(self.projectShellUpdate)
    
    
    def launcherShellUpdate(self, text: str):
        cursor = self.launcherShell.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.launcherShell.setTextCursor(cursor)
        self.launcherShell.ensureCursorVisible()
    
    
    def projectShellUpdate(self, text: str):
        cursor = self.projectShell.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.projectShell.setTextCursor(cursor)
        self.projectShell.ensureCursorVisible()
        
    
    
    def statusUpdate(self):
        self.currentShell = self.Shells.currentWidget().children()[1]
        shellName = self.currentShell.objectName()
        logger.debug(f"控制台名称：{shellName}")
        if shellName == "projectShell":
            self.cmdBar.actions()[2].setText(self.tr("启动器控制台"))
            self.shellName.setText(" 项目")
            if _project.isRunning():
                self.status.setText("运行中")
                self.status.setTextColor(Color.GREEN,Color.GREEN)
            else:
                self.status.setText("未运行")
                self.status.setTextColor(Color.RED, Color.RED)
        else:
            self.shellName.setText("启动器")
            self.cmdBar.actions()[2].setText(self.tr("项目控制台"))
            self.status.setText("运行中")
            self.status.setTextColor(Color.GREEN, Color.GREEN)
        
        
    def clear(self):
        logger.debug(f"清空当前控制台：{self.currentShell.objectName()}")
        self.currentShell.clear()
    
    
    def saveAs(self):
        logger.debug("保存")
    
    
    def switchStream(self):
        logger.debug(f"当前页：{self.Shells.currentIndex()}")
        logger.debug("切换控制台")
        self.Shells.setCurrentIndex(self.Shells.count() - 1 -self.Shells.currentIndex())
        self.statusUpdate()