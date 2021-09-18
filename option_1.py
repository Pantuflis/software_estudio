# Option 1: Add an "A" at the end of each line of the file selected
import os
from PyQt6.QtWidgets import QFileDialog
from elements import SuccessWindow


def process_1(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
    stripped_data = []
    for line in data:
        stripped_data.append(line.strip() + "A" + "\n")
    return stripped_data

    # desktop_path = os.path.join(os.path.join(
    #     os.environ['USERPROFILE']), 'Desktop')
    # file_path = QFileDialog.getSaveFileName(
    #     caption='Open file', directory=desktop_path, filter='*.txt')
    # with open(file_path[0], "w") as final_file:
    #     for line in stripped_data:
    #         final_file.writelines(line)
    # success_window = SuccessWindow()
    # success_window.show()
