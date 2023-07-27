from utils.cep import cadastro_endereco
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import *
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

print("Seja bem-vindo(a) ao Sistema de Gerenciamento de Carteira de Ações da Nuclea. Selecione uma das opções abaixo:")


def cadastro_cliente():
    print("1 - Módulo Cadastro de Clientes - Informe os dados do cliente:")
    cliente = {
        "nome": formata_texto(input("Nome: ")),
        "cpf": valida_cpf(),
        "rg": valida_rg(),
        "data_nascimento": valida_data_nascimento(),
        "endereco": cadastro_endereco(),
    }

    clientes.append(cliente)

    print("Informações do cliente cadastrado:")
    print(cliente)
    global validador
    validador = retornar_menu_principal()


def cadastro_acao():
    print("2 - Cadastrar ação")


def analise():
    print("3 - Realizar análise da carteira")


def imprime_relatorio():
    print("4 - Imprimir relatório da carteira")


validador = True
clientes = []

while (validador):
    print("=== MENU ===")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar ação")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção de 1 a 5: "))

    if opcao == 1:
        cadastro_cliente()
    elif opcao == 2:
        cadastro_acao()
    elif opcao == 3:
        analise()
    elif opcao == 4:
        imprime_relatorio()
    elif opcao == 5:
        sair()
    else:
        print("Opção inválida, tente novamente. Escolha uma opção entre 1 e 5.")
