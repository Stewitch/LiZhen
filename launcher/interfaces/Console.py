from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtCore import Qt
from qfluentwidgets import Action, FluentIcon

from .ui.Ui_Console import Ui_Console
from .Widgets import ExportDialog

from ..utils.log import logger
from ..utils.common import project, switchProjectState, openFolder
from ..utils.stream import _stderr
from ..utils.color import Color
from ..utils.paths import LOGS



class ConsoleInterface(QWidget, Ui_Console):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.__initWidgets()
        self.__initFunctions()
        self.__SSConnection()
        
        self.__updateStatus()
        project.initUV()
        
        
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
            Action(FluentIcon.SAVE_AS, self.tr("导出日志"), triggered=self.saveAs),
        ])
        self.cmdBar.addSeparator()
        self.cmdBar.addActions([
            Action(FluentIcon.PLAY_SOLID, self.tr("一键启动"), triggered=lambda: switchProjectState()),
            Action(FluentIcon.ROTATE, self.tr("启动器控制台"), triggered=self.switchShell)
        ])
    
    
    def __initFunctions(self):
        self.currentShell = self.Shells.currentWidget().children()[1]
        self.stderr = _stderr
    
    
    def __SSConnection(self):
        project.changed.connect(self.__updateStatus)
        project.changed.connect(self.__updateButton)
        project.shellNewText.connect(self.projectShellUpdate)
        self.stderr.newText.connect(self.launcherShellUpdate)
    
    
    def launcherShellUpdate(self, text: str):
        cursor = self.launcherShell.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertHtml(text)
        self.launcherShell.setTextCursor(cursor)
        self.launcherShell.ensureCursorVisible()
    
    
    def projectShellUpdate(self, text: str):
        cursor = self.projectShell.textCursor()
        if '\r' in text:
            # 移动到最后一行开始
            cursor.movePosition(QTextCursor.End)
            cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
            # 删除当前行
            cursor.removeSelectedText()
            # 插入新进度
            cursor.insertHtml(text.replace('\r', ''))
        else:
            cursor.movePosition(QTextCursor.End)
            cursor.insertHtml(text)
        self.projectShell.setTextCursor(cursor)
        self.projectShell.ensureCursorVisible()
    
    
    def __updateButton(self, status: str):
        if status in ["on", "starting"]:
            self.cmdBar.actions()[2].setIcon(FluentIcon.PAUSE_BOLD)
            self.cmdBar.actions()[2].setText(self.tr("终止项目"))
        else:
            self.cmdBar.actions()[2].setIcon(FluentIcon.PLAY_SOLID)
            self.cmdBar.actions()[2].setText(self.tr("一键启动"))

    
    def __updateStatus(self):
        self.currentShell = self.Shells.currentWidget().children()[1]
        shellName = self.currentShell.objectName()
        if shellName == "projectShell":
            self.cmdBar.actions()[3].setText(self.tr("启动器控制台"))
            self.shellName.setText(self.tr(" 项目"))
            if project.isRunning() is None:
                self.status.setText(self.tr("启动中"))
                self.status.setTextColor(Color.GOLD, Color.GOLD)
                self.currentShell.clear()
            elif project.isRunning():
                self.status.setText(self.tr("运行中"))
                self.status.setTextColor(Color.LIME_GREEN,Color.GREEN)
            else:
                self.status.setText(self.tr("未运行"))
                self.status.setTextColor(Color.RED, Color.RED)
        else:
            self.shellName.setText(self.tr("启动器"))
            self.cmdBar.actions()[3].setText(self.tr("项目控制台"))
            self.status.setText(self.tr("运行中"))
            self.status.setTextColor(Color.LIME_GREEN, Color.GREEN)
        
        
    def clear(self):
        logger.debug(f"清空当前控制台：{self.currentShell.objectName()}")
        self.currentShell.clear()
    
    
    def saveAs(self):
        logger.debug("导出日志")
        shellName = self.currentShell.objectName()
        if shellName == "projectShell":
            log = self.projectShell.toHtml()
            with open(LOGS.joinpath("project.html"), 'w', encoding="utf-8") as f:
                f.write(log)
        else:
            w = ExportDialog(
                self.tr("额外导出"),
                self.tr(
                    """
                    完整启动器日志默认保存在 ./luancher/logs/luancher.log 文件中
                    此操作将导出额外的一份并不完整html格式的日志文件(但包含部分Debug信息)
                    是否导出？
                    """
                ),
                self
            )
            if w.exec():
                log = self.launcherShell.toHtml()
                with open(LOGS.joinpath("luancher.html"), "w", encoding="utf-8") as f:
                    f.write(log)

        openFolder(str(LOGS))
    
    
    def switchShell(self):
        self.Shells.setCurrentIndex(self.Shells.count() - 1 -self.Shells.currentIndex())
        self.__updateStatus()
        logger.debug(f"切换控制台到：{self.currentShell.objectName()}")