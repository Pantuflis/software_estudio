import pandas as pd
import os
from PyQt6.QtWidgets import QFileDialog
from elements import SuccessWindow

# Option 4: Convert a excel file from Misiones web into two txt files for import into Misisones web


def process_4_1(file_name):
    # Read file
    df = pd.read_excel(file_name)

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
    date = ret_df["Fecha ret/per"].str[:10]
    bill_number = ret_df["Nro. de comprobante"].str[-9:]
    name = ret_df["Razon social"]
    id = ret_df["Nro. documento"]
    amount = ret_df["Monto sujeto retención"]
    percentage = ret_df["Alicuota IB"]
    data = date + "," + bill_number + "," + name + \
        ", ," + id + "," + amount + "," + percentage

    # Concatenate fields for txt
    txt = []
    for line in data:
        txt.append(line + '\n')
    return txt


def process_4_2(file_name):
    # Read file
    df = pd.read_excel(file_name)

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

    # Concatenate fields for txt
    txt = []
    for line in data:
        txt.append(line + '\n')
    return txt

    # Save txt
    #     if round == 1:
    #         desktop_path = os.path.join(os.path.join(
    #             os.environ['USERPROFILE']), 'Desktop')
    #         file_path = QFileDialog.getSaveFileName(
    #             caption='Open file', directory=desktop_path, filter='*.txt')
    #         success_window = SuccessWindow()
    #         success_window.show()
    #     elif round == 2:
    #         desktop_path = os.path.join(os.path.join(
    #             os.environ['USERPROFILE']), 'Desktop')
    #         file_path = QFileDialog.getSaveFileName(
    #             caption='Open file', directory=desktop_path, filter='*.txt')
    #         success_window.show()
    #     with open(file_path[0], "w") as final_file:
    #         for i in range(len(txt)):
    #             final_file.writelines(txt[i]+"\n")
    # success_window = SuccessWindow()
    # success_window.show()
