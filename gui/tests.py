import pandas as pd
import sys
import os
from elements import ErrorWindow, MainWindow, Button
from PyQt6.QtWidgets import QApplication, QFileDialog
# from option_4 import process_4

app = QApplication(sys.argv)
window = MainWindow()
button = Button('OK')
window.global_layout.addWidget(button)


error_window = ErrorWindow()
error_window.display_error(
    '<PyQt6.QtCore.QMetaObject.Connection object at 0x000001D15461E5F0>')


def process_4():
    # Read file
    df = pd.read_excel('../MISIONES MAYO 2021.xlsx')

    # Create a df for retentions and perceptions
    ret_df = pd.DataFrame(df[df["Origen"] == "Compras"])
    percep_df = pd.DataFrame(df[df["Origen"] == "Ventas"])

    # Convert DF columns into necessary format
    for column in ret_df.columns:
        ret_df[column] = ret_df[column].astype(str)
    for column in ret_df.columns:
        percep_df[column] = percep_df[column].astype(str)
    ret_df["Fecha ret/per"] = ret_df["Fecha ret/per"].apply(
        lambda x: x.replace("/", "-"))

    # Build all the fields for txt
    round = 0
    while round <= 1:
        if round == 0:
            date = ret_df["Fecha ret/per"].str[:10]
            bill_number = ret_df["Nro. de comprobante"].str[-9:]
            name = ret_df["Razon social"]
            id = ret_df["Nro. documento"]
            amount = ret_df["Monto sujeto retención"]
            percentage = ret_df["Alicuota IB"]
            data = date + "," + bill_number + "," + name + \
                ", ," + id + "," + amount + "," + percentage
            round += 1
        elif round == 1:
            date = percep_df["Fecha ret/per"].str[:10]
            bill_type = percep_df["Tipo"].str[:2] + \
                "_" + percep_df["Nro. de comprobante"].str[:1]
            bill_number = percep_df["Nro. de comprobante"].str[-9:]
            name = percep_df["Razon social"]
            id = percep_df["Nro. documento"]
            amount = percep_df["Monto sujeto retención"]
            percentage = percep_df["Alicuota IB"]
            data = date + "," + bill_type + "," + bill_number + "," + name + \
                "," + id + "," + amount + "," + percentage
            round += 1

        # Concatenate fields for txt
        txt = []
        for line in data:
            txt.append(line)

    # Save txt
    if round == 1:
        desktop_path = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        file_path = QFileDialog.getSaveFileName(
            caption='Open file', directory=desktop_path, filter='*.txt')
    elif round == 2:
        desktop_path = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        file_path = QFileDialog.getSaveFileName(
            caption='Open file', directory=desktop_path, filter='*.txt')
    with open(file_path[0], "w") as final_file:
        for i in range(len(txt)):
            final_file.writelines(txt[i]+"\n")


button.clicked.connect(process_4)

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())
