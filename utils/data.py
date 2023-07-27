import re
from datetime import datetime


def valida_data_nascimento():
    while True:

        data_nascimento = input("Data Nascimento: ")

        try:

            if re.match(r'(\d{2})/(\d{2})/(\d{2,4})', data_nascimento):
                pass
            else:
                data_nascimento = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"

            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual.")
        except ValueError as e:
            print(f"Erro: {e}.")
            print("Data inválida, tente novamente.")


if __name__ == "__main__":
    valida_data_nascimento()
