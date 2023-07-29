import requests
from utils.funcoes_auxiliares import retornar_menu


def valida_cep():
    while True:
        cep = input("Digite seu cep para buscar o endereço: ")
        cep.replace("/[^0-9]/", "")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                endereco = {
                    "CEP": data['cep'],
                    "Logradouro": data['logradouro'],
                    "Numero": ['numero'],
                    'Complemento': data['complemento'],
                    "Bairro": data['bairro'],
                    "Cidade": data['localidade'],
                    "Estado": data['uf'],
                    'DDD': data['ddd']
                }
                return endereco
            else:
                print("CEP inválido. Tente novamente.")
        else:
            print("CEP inválido. Tente novamente.")


def cadastro_endereco():
    while True:
        endereco = valida_cep()
        endereco['Numero'] = input("Número da residência: ")
        endereco['Complemento'] = input("Complemento: ")
        return retornar_menu(endereco, cadastro_endereco)


if __name__ == "__main__":
    cadastro_endereco()
