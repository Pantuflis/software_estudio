# Option 1: Add an "A" at the end of each line of the file selected
import os
from PyQt6.QtWidgets import QFileDialog
from elements import SuccessWindow


# def process_1():
#     print("")
#     file_name = input("Input the file name: ")
#     print("")
#     if file_name[-4:] != ".txt":
#         file_name = file_name + ".txt"
#     with open(file_name, "r") as file:
#         data = file.readlines()
#         stripped_data = []
#         for line in data:
#             stripped_data.append(line.strip() + "A" + "\n")
#         save_txt(stripped_data)


# def save_txt(data):
#     file_name = input("\nInput the name to save the file: ")
#     if file_name[-4:] != ".txt":
#         file_name = file_name + ".txt"
#     with open(file_name, "w") as final_file:
#         final_file.writelines(data)
#     print("\nFile successfully saved")


def process_1(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
    stripped_data = []
    for line in data:
        stripped_data.append(line.strip() + "A" + "\n")
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = QFileDialog.getSaveFileName(
        caption='Open file', directory=desktop_path, filter='*.txt')
    with open(file_path[0], "w") as final_file:
        final_file.writelines(stripped_data)
    success_window = SuccessWindow()
    success_window.show()
