import os
from PyQt6.QtWidgets import QFileDialog
from elements import BrowseBar


def browse_file():
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = QFileDialog.getOpenFileName(
        caption='Open file', directory=desktop_path, filter='*.txt *.xlsx *.xls')
    browser_bar = BrowseBar()
    browser_bar.setText(file_path[0])
