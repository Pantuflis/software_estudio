import pandas as pd

# Option 4: Convert a excel file from Misiones web into two txt files for import into Misisones web


def option_4():
    print("")
    file_name = input("Input the file name: ")
    print("")
    if file_name[-4:] != ".xls" or file_name[-5:] != ".xlsx":
        file_name = file_name + ".xlsx"

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
        save_txt(txt, round)


def save_txt(data, round):
    if round == 1:
        file_name = input('\nInput the name to save the "Retenciones" file: ')
    elif round == 2:
        file_name = input('\nInput the name to save the "Percepciones" file: ')
    if file_name[-4:] != ".txt":
        file_name = file_name + ".txt"
    with open(file_name, "w") as final_file:
        for i in range(len(data)):
            final_file.writelines(data[i]+"\n")
    print("\nFile successfully saved\n\n")
