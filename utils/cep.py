import requests
import json
from utils.funcoes_auxiliares import retornar_menu


def valida_cep():
    while True:
        cep = input("Digite seu cep para buscar o endereço: ")
        cep.replace("/[^0-9]/", "")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            endereco = json.loads(response.text)
            if 'erro' in endereco:
                print("CEP inválido. Tente novamente.")
            else:
                return endereco
        else:
            print("CEP inválido. Tente novamente.")


def cadastro_endereco():
    while True:
        endereco = valida_cep()
        endereco['numero'] = input("Digite o numero de sua residência: ")
        endereco['complemento'] = input("Complemento: ")
        return retornar_menu(endereco, cadastro_endereco)


if __name__ == "__main__":
    cadastro_endereco()
