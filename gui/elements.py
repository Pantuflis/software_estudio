import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QFrame, QMainWindow, QCheckBox
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QCursor
from PyQt6 import QtWidgets


class Button(QPushButton):
    def __init__(self, btn_name=""):
        super().__init__(btn_name)
        self.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet(
            """*{border: 4px solid 'green';
            border-radius: 35px;
            font-size: 35px;
            color: 'white';
            padding: 10px 0;
            margin: 100px 100px;}
            *:hover{background: 'green'}
            *:pressed{background: 'lightgreen'}"""
        )
        # self.clicked.connect(self.check)

    def check(self, option):
        option()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pantuflis Software")
        self.setFixedWidth(1000)
        self.setStyleSheet("background: 'black';")
        self.grid = QGridLayout()
        self.setLayout(self.grid)


# System
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
