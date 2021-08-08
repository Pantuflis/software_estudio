from options.option_1 import option_1
from options.option_2 import option_2
from options.option_3 import option_3
from options.option_4 import option_4
import os
import time


def menu():
    os.system("cls")
    option = int(input(
        "WELCOME!\n[1] Archivo Grupos Integrados\n[2] SIFERE - Retenciones AGIP\n[3] SIFERE - Percepciones AGIP\n[4] Agente de Recaudacion Misiones\n\nSelect an option [1/2/3/4]: "))
    return option


def convert_txt():
    option = menu()
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    else:
        print("Please select a valid option")
        time.sleep(2)
        convert_txt()


def run():
    convert_txt()


if __name__ == "__main__":
    run()
