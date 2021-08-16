import os
import time
import sys
from PyQt6.QtWidgets import QApplication
from elements import App, MainWindow, BrowseBar, Button, ProgressBar, Options
from PyQt6 import QtGui, QtCore

# Create application adn window
app = QApplication(sys.argv)
window = MainWindow()

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

# Display element in window
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
convert_btn.clicked.connect(run)


if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())
