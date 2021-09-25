import pandas as pd
import os
from PyQt6.QtWidgets import QFileDialog
from elements import SuccessWindow

# Option 2: Convert the csv file of retentions from AGIP into a txt for importing to SIFERE


def process_2(file_name):
    # Sometime thw downloaded file has a first line that must be removed in order to the rest of the program work
    with open(file_name, 'r') as f:
        lines = f.readlines()
        if '=' in lines[0]:
            lines.pop(0)

    with open(file_name, 'w') as f:
        for line in lines:
            f.write(line)

    # Read the csv file and create a DF
    ret_df = pd.DataFrame(pd.read_csv(file_name, index_col=False))

    # Convert DF columns into necessary format
    for column in ret_df.columns:
        ret_df[column] = ret_df[column].astype(str)

    ret_df["N° Ader"] = ret_df["N° Ader"].apply(lambda x: "0" + str(x))
    ret_df["Tipo Comprobante"] = ret_df["Tipo Comprobante"].apply(
        lambda x: x.replace("X", "O").replace("L", "O").replace("R", "O"))
    ret_df["N° Comprobante"] = ret_df["N° Comprobante"].apply(
        lambda x: x.zfill(16).replace(" ", "0").replace("A", "0"))
    ret_df["N° Certificado"] = ret_df["N° Certificado"].apply(
        lambda x: x.replace("-", "").replace("ORDD", "").zfill(20))
    ret_df["Monto Retenido"] = ret_df["Monto Retenido"].apply(
        lambda x: x.replace(".", ","))

    # Build the fields for txt
    jurisdiction = "90100"
    cuit = ret_df["CUIT"]
    date = ret_df["Fecha Retencion"]
    succursal = ret_df["N° Ader"].str[-4:]
    bill_number = ret_df["N° Comprobante"].str[-16:]
    bill_type = ret_df["Tipo Comprobante"]
    bill_letter = "A"
    certificate = ret_df["N° Certificado"]
    retention = ret_df["Monto Retenido"]

    # After create retention field iterate and split de values to add 00 at the end
    decimals = []
    for i in range(len(retention)):
        decimals.append(retention[i].split(","))
        for j in range(len(decimals)):
            if len(decimals[j][1]) < 2:
                decimals[j][1] = decimals[j][1] + "0"
    for i in range(len(decimals)):
        retention[i] = (",".join(decimals[i]).zfill(11))

    # Create th final string with all the info
    data = jurisdiction + cuit + date + succursal + bill_number + \
        bill_type + bill_letter + certificate + retention

    # Concatenate fields for txt
    txt = []
    for line in data:
        txt.append(line + "\n")
    return txt
