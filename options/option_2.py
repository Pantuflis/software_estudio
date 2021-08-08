import pandas as pd

# Option 2: Convert the csv file of retentions from AGIP into a txt for importing to SIFERE


def option_2():
    print("")
    file_name = input("Input the file name: ")
    print("")
    if file_name[-3:] != ".csv":
        file_name = file_name + ".csv"

    # Read the csv file and create a DF
    ret_df = pd.DataFrame(pd.read_csv("RentasCiudad.csv", index_col=False))

    # Convert DF columns into necessary format
    for column in ret_df.columns:
        ret_df[column] = ret_df[column].astype(str)

    ret_df["N° Ader"] = ret_df["N° Ader"].apply(lambda x: "0" + str(x))
    ret_df["Tipo Comprobante"] = ret_df["Tipo Comprobante"].apply(
        lambda x: x.replace("X", "O"))
    ret_df["N° Comprobante"] = ret_df["N° Comprobante"].apply(
        lambda x: x.zfill(16).replace(" ", "0").replace("A", "0"))
    ret_df["N° Certificado"] = ret_df["N° Certificado"].apply(
        lambda x: x.zfill(20))
    ret_df["Monto Retenido"] = ret_df["Monto Retenido"].apply(
        lambda x: x.replace(".", ","))

    # Build the fields for txt
    jurisdiction = "90100"
    cuit = ret_df["CUIT"]
    date = ret_df["Fecha Comprobante"]
    succursal = ret_df["N° Ader"].str[-4:]
    bill_number = ret_df["N° Comprobante"]
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
                decimals[j][1] = "00"
    for i in range(len(decimals)):
        retention[i] = (",".join(decimals[i]).zfill(11))

    # Create th final string with all the info
    data = jurisdiction + cuit + date + succursal + bill_number + \
        bill_type + bill_letter + certificate + retention

    # Concatenate fields for txt
    txt = []
    for line in data:
        txt.append(line + "\n")
    save_txt(txt)


def save_txt(data):
    file_name = input("\nInput the name to save the file: ")
    if file_name[-4:] != ".txt":
        file_name = file_name + ".txt"
    with open(file_name, "w") as final_file:
        final_file.writelines(data)
    print("\nFile successfully saved")
