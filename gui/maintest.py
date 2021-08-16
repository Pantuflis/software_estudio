import os
import sys
from PyQt6.QtWidgets import QApplication, QProgressBar, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QFrame, QMainWindow, QCheckBox, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QCursor
from PyQt6 import QtWidgets
from elements import MainWindow, Button


widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
}

# Create window with black background
app = QApplication(sys.argv)
window = MainWindow()


def start_game():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(len(widgets[widget])):
            widgets[widget].pop()
    frame_2()


def create_buttons(btn_name):
    answer_button = Button(btn_name)
    answer_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    answer_button.setFixedWidth(485)
    return answer_button


def save_file():
    file_name = QFileDialog.getSaveFileName()
    print(file_name)
    return file_name


def frame_1():
    # Display logo
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 50px")
    widgets['logo'].append(logo)

    def select_file():
        desktop_path = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        file_name = QFileDialog.getOpenFileName(
            caption='Open File', directory=desktop_path, filter='*.txt *.xlsx')
        dir_path.setText(file_name[0])
        dir_path.show()

    # Buttons
    ok_button = Button("OK")
    ok_button.clicked.connect(select_file)
    cancel_button = Button("Cancel")
    cancel_button.clicked.connect(save_file)
    widgets['button'].append(ok_button)

    # Browse
    dir_path = QLineEdit()

    # Progress Bar
    bar = QProgressBar()

    # Grid
    window.grid.addWidget(widgets['logo'][-1], 0, 0, 1, 2)
    window.grid.addWidget(widgets['button'][-1], 1, 0)
    window.grid.addWidget(cancel_button, 1, 1)
    window.grid.addWidget(dir_path, 2, 0, 1, 2)
    window.grid.addWidget(bar, 3, 0, 1, 2)


def frame_2():
    score = QLabel('80')
    score.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    score.setStyleSheet(
        """border: 1px solid 'green';
           border-radius: 35px;
           background-color: 'green'; 
           font-size: 35px;
           color: 'white';
           padding: 20px 15px;
           margin: 100px 200px;"""
    )
    widgets['score'].append(score)

    question = QLabel('Place holder')
    question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        """font-family: Shanti;
        font-size: 25px;
        color: 'white';
        padding: 75px;"""
    )
    widgets['question'].append(question)

    button1 = create_buttons('answer1')
    button2 = create_buttons('answer2')
    button3 = create_buttons('answer3')
    button4 = create_buttons('answer4')

    widgets['answer1'].append(button1)
    widgets['answer2'].append(button2)
    widgets['answer3'].append(button3)
    widgets['answer4'].append(button4)

    window.grid.addWidget(widgets['score'][-1], 0, 1)
    window.grid.addWidget(widgets['question'][-1], 1, 0, 1, 2)
    window.grid.addWidget(widgets['question'][-1], 1, 0, 1, 2)
    window.grid.addWidget(widgets['answer1'][-1], 2, 0)
    window.grid.addWidget(widgets['answer2'][-1], 2, 1)
    window.grid.addWidget(widgets['answer3'][-1], 3, 0)
    window.grid.addWidget(widgets['answer4'][-1], 3, 1)


if __name__ == "__main__":
    frame_1()
    window.show()
    sys.exit(app.exec())
