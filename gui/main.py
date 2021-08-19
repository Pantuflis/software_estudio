import time
import os
import sys
from PyQt6.QtWidgets import QApplication
from elements import App, MainWindow, BrowseBar, Button, ProgressBar, Options, QFileDialog, ErrorWindow, SuccessWindow, InfoWindow
from option_1 import process_1
from option_2 import process_2
from option_3 import process_3
from option_4 import process_4

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
info_window = InfoWindow()

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


def run():
    progress_bar.setRange(0, 10)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.setValue(i+1)
        app.processEvents()


# Functions
def browse_file(filter):
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = QFileDialog.getOpenFileName(
        caption='Open file', directory=desktop_path, filter=filter)
    browser_bar.setText(file_path[0])


def filter():
    if option_1.isChecked():
        browse_file('*.txt')
    elif option_2.isChecked() or option_3.isChecked():
        browse_file('*.csv')
    elif option_4.isChecked():
        browse_file('*.xlsx')
    else:
        info_window.show()


def convert_process(file_name):
    if option_1.isChecked():
        try:
            process_1(file_name)
        except UnicodeDecodeError as e:
            error_window.display_error(
                f'{str(e)}\n Please select a valid txt file')
            error_window.show()
    elif option_2.isChecked():
        try:
            process_2(file_name)
        except KeyError as e:
            error_window.display_error(
                f'Missing column {str(e)}\n Please select a valid csv file')
            error_window.show()
    elif option_3.isChecked():
        try:
            process_3(file_name)
        except KeyError as e:
            error_window.display_error(
                f'Missing column {str(e)}\n Please select a valid csv file')
            error_window.show()
    elif option_4.isChecked():
        try:
            process_4(file_name)
        except KeyError as e:
            error_window.display_error(
                f'Missing column {str(e)}\n Please select a valid xlsx file')
    else:
        pass


browse_btn.clicked.connect(filter)
convert_btn.clicked.connect(lambda: convert_process(browser_bar.text()))

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())
