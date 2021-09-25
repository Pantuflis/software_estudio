import sys
from PyQt6.QtWidgets import QApplication, QGroupBox, QLabel, QMessageBox, QPushButton, QWidget, QFileDialog, QGridLayout, QLineEdit, QProgressBar, QRadioButton, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QCursor
from PyQt6 import QtWidgets

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pantuflis Software")
        self.setFixedSize(500, 300)
        self.setStyleSheet('background: #3b444b;')
        # Change logo fir definitive
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.global_layout = QVBoxLayout()
        self.op_container = QGroupBox("Options")
        self.op_container_layout = QGridLayout()
        self.op_container.setLayout(self.op_container_layout)
        self.op_container.setStyleSheet(
            """*{border: 1.5px solid '#0e1111';
            border-radius: 4px;
            color: 'white';
            font-size: 15px;
            margin: 5px 0 0 0;
            padding: 0 10px 0 10px;}
            *::title {
                top: -8px;
                left: 10px;
                }"""
        )
        self.options_layout = QGridLayout()
        self.process_layout = QGridLayout()
        self.global_layout.setSpacing(0)
        self.global_layout.setContentsMargins(5, 10, 5, 10)  # L, T, R, B
        self.op_container_layout.setSpacing(0)
        self.op_container_layout.setContentsMargins(5, 0, 5, 0)
        self.options_layout.setSpacing(0)
        self.options_layout.setContentsMargins(0, 0, 0, 0)
        self.process_layout.setSpacing(0)
        self.process_layout.setContentsMargins(0, 15, 0, 10)
        self.process_layout.setSpacing(20)
        self.setLayout(self.global_layout)

class BrowseBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 35)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet(
            """border: 2px solid '#0e1111';
            background-color: '#232b2b';
            border-radius: 7px;
            color: 'white';
            font-size: 15px;
            margin: 0;"""
        )


class Button(QPushButton):
    def __init__(self, text="", width=100, height=100, radius='10', font_size='10', t_margin='0', b_margin='0', r_margin='0', l_margin='0'):
        super().__init__()
        self.setText(text)
        self.setFixedSize(width, height)
        self.setStyleSheet(
            "*{border: 3px solid '#68a7ff';" +
            f"border-radius: {radius}px;" +
            "background: '#68a7ff';" +
            "font-weight: bold;" +
            "font-family: 'Arial';" +
            f"font-size: {font_size}px;" +
            "color: 'white';" +
            f"margin-right: {r_margin}px;" +
            f"margin-left: {l_margin}px;" +
            f"margin-top: {t_margin}px;" +
            f"margin-bottom: {b_margin}px;" +
            "padding: 5px 5px;}" +
            "*:hover{background: '#2f6ec5'}" +
            "*:hover{border: '#2f6ec5'}" +
            "*:pressed{background: '#1c4e94'}"
        )


class ProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """ProgressBar{border: 2px solid '#0e1111';
            background-color: '#232b2b';
            border-radius: 7px;
            color: 'white';
            font-size: 15px;
            font-weight: bold;
            text-align: center;}
            *::chunk{
                background-color: '#8237f9';
                border-radius: 4px;
                }"""
        )
        self.setValue(0)


class Options(QRadioButton):
    def __init__(self, text=""):
        super().__init__()
        self.setText(text)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(
            """border: 0;
            color: 'white';
            margin: 0;
            padding: 0;"""
        )


class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Something went wrong")
        self.setStyleSheet(
            """background: #3b444b;
            color: white;
            font-size: 15px;"""
        )
        self.message_layout = QVBoxLayout()
        self.btn_layout = QGridLayout()
        self.setLayout(self.message_layout)
        self.error = QLabel()
        self.error.setText('Error')
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ok_button = Button(text='OK', width=100,
                                height=40, font_size='15')
        # self.ok_button.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message_layout.addWidget(self.error)
        self.message_layout.addLayout(self.btn_layout)
        self.btn_layout.addWidget(self.ok_button)
        self.btn_layout.setContentsMargins(10, 20, 10, 10)
        self.ok_button.clicked.connect(lambda: self.close())

    def display_error(self, error=''):
        self.error.setText(error)


class SuccessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Success!")
        self.setStyleSheet(
            """background: #3b444b;
            color: white;
            font-size: 15px;"""
        )
        self.message_layout = QVBoxLayout()
        self.btn_layout = QGridLayout()
        self.setLayout(self.message_layout)
        self.error = QLabel()
        self.error.setText('File successfully converted and saved')
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ok_button = Button(text='OK', width=100,
                                height=40, font_size='15')
        self.message_layout.addWidget(self.error)
        self.message_layout.addLayout(self.btn_layout)
        self.btn_layout.addWidget(self.ok_button)
        self.btn_layout.setContentsMargins(10, 20, 10, 10)
        self.ok_button.clicked.connect(lambda: self.close())


class InfoWindow(QWidget):
    def __init__(self, text=''):
        super().__init__()
        self.setWindowTitle("Important information")
        self.setStyleSheet(
            """background: #3b444b;
            color: white;
            font-size: 15px;"""
        )
        self.message_layout = QVBoxLayout()
        self.btn_layout = QGridLayout()
        self.setLayout(self.message_layout)
        self.error = QLabel()
        self.error.setText(text)
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ok_button = Button(text='OK', width=100,
                                height=40, font_size='15')
        # self.ok_button.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message_layout.addWidget(self.error)
        self.message_layout.addLayout(self.btn_layout)
        self.btn_layout.addWidget(self.ok_button)
        self.btn_layout.setContentsMargins(10, 20, 10, 10)
        self.qr = self.frameGeometry()
        self.center = QApplication.primaryScreen().availableGeometry().center()
        self.qr.moveCenter(self.center)
        self.move(self.qr.topLeft())
        self.ok_button.clicked.connect(lambda: self.close())
