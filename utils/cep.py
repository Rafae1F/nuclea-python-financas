import requests
from utils.funcoes_auxiliares import retornar_menu


def valida_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Numero": [''],
                'Complemento': data['complemento'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf'],
                'DDD': data['ddd']
            }

            return endereco


def cadastro_endereco():
    print("Consulta do CEP - ViaCEP")

    while True:
        cep = input("Digite seu cep para buscar o endereço: ")
        cep = "".join(digito for digito in cep if digito.isdigit())
        if cep.isdigit() and len(cep) == 8:
            endereco = valida_cep(cep)
            if endereco:
                endereco['Numero'] = input("Número da residência: ")
                endereco['Complemento'] = input("Complemento: ")
                return retornar_menu(endereco, cadastro_endereco)
            else:
                print("CEP não encontrado ou inválido")
        else:
            print("CEP não encontrado ou inválido")


if __name__ == "__main__":
    cadastro_endereco()
