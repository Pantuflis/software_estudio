import pandas as pd
import os
from PyQt6.QtWidgets import QFileDialog
from elements import SuccessWindow

# Option 2: Convert the csv file of perceptions from AGIP into a txt for importing to SIFERE


def process_3(file_name):
    # Sometime thw downloaded file has a first line that must be removed in order to the rest of the program work
    with open(file_name, 'r') as f:
        lines = f.readlines()
        if '=' in lines[0]:
            lines.pop(0)

    with open(file_name, 'w') as f:
        for line in lines:
            f.write(line)

    # Read the csv file and create a DF
    percep_df = pd.DataFrame(pd.read_csv(
        file_name, index_col=False))

    # Convert DF columns into necessary format
    for column in percep_df.columns:
        percep_df[column] = percep_df[column].astype(str)

    percep_df["N° Ader"] = percep_df["N° Ader"].apply(lambda x: "0" + str(x))
    percep_df["Tipo Comprobante"] = percep_df["Tipo Comprobante"].apply(
        lambda x: x.replace("X", "O"))
    percep_df["N° Comprobante"] = percep_df["N° Comprobante"].apply(
        lambda x: x.zfill(8).replace(" ", "0").replace("A", "0"))
    percep_df["Monto Percibido"] = percep_df["Monto Percibido"].apply(
        lambda x: x.replace(".", ","))

    # Build the fields for txt
    jurisdiction = "90100"
    cuit = percep_df["CUIT"]
    date = percep_df["Fecha Percepcion"]
    succursal = percep_df["N° Ader"].str[-4:]
    bill_number = percep_df["N° Comprobante"].str[-8:]
    bill_type = percep_df["Tipo Comprobante"]
    bill_letter = "A"
    perception = percep_df["Monto Percibido"]

    # After create perception field iterate and split de values to add 00 at the end
    decimals = []
    for i in range(len(perception)):
        decimals.append(perception[i].split(","))
        for j in range(len(decimals)):
            if len(decimals[j][1]) < 2:
                decimals[j][1] = "00"
    for i in range(len(decimals)):
        perception[i] = (",".join(decimals[i]).zfill(11))

    # Create th final string with all the info
    data = jurisdiction + cuit + date + succursal + bill_number + \
        bill_type + bill_letter + perception

    # Concatenate fields for txt
    txt = []
    for line in data:
        txt.append(line + "\n")
    return txt
