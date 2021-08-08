# Option 1: Add an "A" at the end of each line of the file selected

def option_1():
    print("")
    file_name = input("Input the file name: ")
    print("")
    if file_name[-4:] != ".txt":
        file_name = file_name + ".txt"
    with open(file_name, "r") as file:
        data = file.readlines()
        stripped_data = []
        for line in data:
            stripped_data.append(line.strip() + "A" + "\n")
        save_txt(stripped_data)


def save_txt(data):
    file_name = input("\nInput the name to save the file: ")
    if file_name[-4:] != ".txt":
        file_name = file_name + ".txt"
    with open(file_name, "w") as final_file:
        final_file.writelines(data)
    print("\nFile successfully saved")
