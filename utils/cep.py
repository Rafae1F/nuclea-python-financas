import requests
import json


def valida_cep():
    while True:
        cep = input("Digite seu cep para buscar o endereço: ")
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
        print(endereco['logradouro'])
        retorna_menu_endereco = input("O endereço acima está correto? Digite (s)im ou (n)ão ").lower()
        if retorna_menu_endereco == "sim" or retorna_menu_endereco == "s":
            return endereco
        elif retorna_menu_endereco == "nao" or retorna_menu_endereco == "n":
            print("Tente novamente. ")
        else:
            print("Opção inválida, tente novamente. Digite 'sim' ou 'não'.")


if __name__ == "__main__":
    cadastro_endereco()
