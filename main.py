import time
import os
import sys
from pandas.errors import ParserError
from PyQt6.QtWidgets import QApplication
from elements import MainWindow, BrowseBar, Button, ProgressBar, Options, QFileDialog, ErrorWindow, SuccessWindow, InfoWindow
from option_1 import process_1
from option_2 import process_2
from option_3 import process_3
from option_4 import process_4_1, process_4_2

# Create application and window
app = QApplication(sys.argv)
window = MainWindow()
window2 = MainWindow()


# Create elements for window
option_1 = Options('Archivo Grupos Integrados')
option_2 = Options('SIFERE - Retenciones AGIP')
option_3 = Options('SIFERE - Percepciones AGIP')
option_4 = Options('Agente de Recaudacion Misiones')
browser_bar = BrowseBar()
browse_btn = Button('BROWSE', width=90, height=35, radius='10', font_size='12')
convert_btn = Button('CONVERT', width=400, height=50,
                     radius='10', font_size='25', l_margin='90', r_margin='0')
progress_bar = ProgressBar()
error_window = ErrorWindow()
success_window = SuccessWindow()

# Display elements in window
window.global_layout.addLayout(window.options_layout)
window.global_layout.addWidget(window.op_container)
window.op_container_layout.addWidget(option_1, 0, 0)
window.op_container_layout.addWidget(option_2, 0, 1)
window.op_container_layout.addWidget(option_3, 1, 0)
window.op_container_layout.addWidget(option_4, 1, 1)
window.global_layout.addLayout(window.process_layout)
window.process_layout.addWidget(browser_bar, 0, 0)
window.process_layout.addWidget(browse_btn, 0, 1)
window.process_layout.addWidget(convert_btn, 1, 0, 1, 2)
window.process_layout.addWidget(progress_bar, 2, 0, 2, 2)


# Functions
def save_file(data):
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = QFileDialog.getSaveFileName(
        caption='Open file', directory=desktop_path, filter='*.txt')
    bar_metter = 1
    progress_bar.setRange(0, len(data))
    with open(file_path[0], "w") as final_file:
        for line in data:
            progress_bar.setValue(bar_metter)
            bar_metter += 1
            final_file.writelines(line)
    success_window.show()


def browse_file(filter):
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = QFileDialog.getOpenFileName(
        caption='Open file', directory=desktop_path, filter=filter)
    browser_bar.setText(file_path[0])
    progress_bar.setValue(0)


def filter():
    if option_1.isChecked():
        browse_file('*.txt')
    elif option_2.isChecked() or option_3.isChecked():
        browse_file('*.csv')
    elif option_4.isChecked():
        browse_file('*.xlsx')
    else:
        info_window = InfoWindow(
            'Please select an option before browse your file')
        info_window.show()


def convert_option_1(file_name):
    try:
        data = process_1(file_name)
        save_file(data)
        browser_bar.setText('')
    except UnicodeDecodeError as e:
        error_window.display_error(
            f'{str(e)}\n Please select a valid txt file')
        error_window.show()

def convert_option_2(file_name):
    try:
        data = process_2(file_name)
        save_file(data)
        browser_bar.setText('')
    except (KeyError, ParserError) as e:
        error_window.display_error(
            f'Missing column {str(e)}\n Please select a valid csv file')
        error_window.show()

def convert_option_3(file_name):
    try:
        data = process_3(file_name)
        save_file(data)
        browser_bar.setText('')
    except (KeyError, ParserError) as e:
        error_window.display_error(
            f'Missing column {str(e)}\n Please select a valid csv file')
        error_window.show()

def convert_option_4(file_name):
    try:
        data = process_4_1(file_name)
        save_file(data)
        data = process_4_2(file_name)
        save_file(data)
        browser_bar.setText('')
    except KeyError as e:
        error_window.display_error(
            f'Missing column {str(e)}\n Please select a valid xlsx file')
        error_window.show()

def show_open_file_error(e):
    error_window.display_error(f'{str(e)}\nFile in use, please close it and retry')
    error_window.show()

def convert_process(file_name):
    try:
        if option_1.isChecked():
            try:
                convert_option_1(file_name)
            except OSError as e:
                show_open_file_error(e)
        elif option_2.isChecked():
            try:
                convert_option_2(file_name)
            except OSError as e:
                show_open_file_error(e)
        elif option_3.isChecked():
            try:
                convert_option_3(file_name)
            except OSError as e:
                show_open_file_error(e)
        elif option_4.isChecked():
            try:
                convert_option_4(file_name)
            except OSError as e:
                show_open_file_error(e)
        else:
            info_window = InfoWindow(
                'Please select an option before convert your file')
            info_window.show()
    except FileNotFoundError as e:
        error_window.display_error('Please select a file before convert')
        error_window.show()


browse_btn.clicked.connect(filter)
convert_btn.clicked.connect(lambda: convert_process(browser_bar.text()))

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())
