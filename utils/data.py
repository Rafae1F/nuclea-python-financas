import re
from datetime import datetime


def valida_data_nascimento():
    while True:
        data_nascimento = input("Data Nascimento: ")
        data_nascimento_mascarada = mascara_data(data_nascimento)
        if valida_data(data_nascimento_mascarada):
            return data_nascimento_mascarada


def valida_data_compra():
    while True:
        data_compra = input("Data da compra: ")
        data_compra_mascarada = mascara_data(data_compra)
        if valida_data(data_compra_mascarada):
            return data_compra_mascarada


def valida_data_inicio():
    while True:
        data_compra = input("Data de inicio: ")
        data_compra_mascarada = mascara_data(data_compra)
        if valida_data(data_compra_mascarada):
            return data_compra_mascarada


def valida_data_fim():
    while True:
        data_compra = input("Data de fim: ")
        data_compra_mascarada = mascara_data(data_compra)
        if valida_data(data_compra_mascarada):
            return data_compra_mascarada


def mascara_data(data_informada):
    if re.match(r'(\d{2})/(\d{2})/(\d{2,4})', data_informada):
        return data_informada
    else:
        return f"{data_informada[:2]}/{data_informada[2:4]}/{data_informada[4:]}"


def valida_data(data_informada):
    try:
        data_convertida = datetime.strptime(data_informada, "%d/%m/%Y").date()
        data_atual = datetime.now().date()
        if data_convertida <= data_atual:
            return data_convertida.strftime("%d/%m/%Y")
        else:
            print("A data informada não pode ser maior que a data atual.")
            return False
    except ValueError:
        print("Data inválida. Certifique-se de informar a data no formato dd/mm/aaaa.")
        return False


def converte_data_alt(data_informada):
    try:
        data_objeto = datetime.strptime(data_informada, '%d/%m/%Y')
        data_informada = data_objeto.strftime('%Y-%m-%d')
        return data_informada
    except ValueError:
        return "Formato de data inválido. Use o formato d/m/Y."


if __name__ == "__main__":
    valida_data_nascimento()
