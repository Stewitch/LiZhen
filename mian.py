from PySide6.QtWidgets import QApplication
from interfaces.MainWindow import MainWindow

def main():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()