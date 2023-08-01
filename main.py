from utils.funcoes_auxiliares import *
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.data import valida_data_nascimento, valida_data_compra
from utils.cep import cadastro_endereco

print("Seja bem-vindo(a) ao Sistema de Gerenciamento de Carteira de Ações da Nuclea. Selecione uma das opções abaixo:")


def menu_principal():
    validador = True
    while validador:
        print("=============== MENU ===============")
        print("1 - Cliente")
        print("2 - Cadastrar ação")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção de 1 a 5: "))

        if opcao == 1:
            submenu_cliente()
        elif opcao == 2:
            cadastro_acao()
        elif opcao == 3:
            analise()
        elif opcao == 4:
            imprime_relatorio()
        elif opcao == 5:
            print("Sair")
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida, tente novamente. Escolha uma opção entre 1 e 5.")


def submenu_cliente():
    while True:
        print("=========== MENU CLIENTE ===========")
        print("1 - Cadastrar cliente")
        print("2 - Consultar cliente")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - Retornar ao menu principal")

        opcao = int(input("Escolha uma opção de 1 a 5: "))
        if opcao == 1:
            cadastro_cliente()
        elif opcao == 2:
            consulta_cliente()
        elif opcao == 3:
            atualizar_cliente()
        elif opcao == 4:
            deletar_cliente()
        elif opcao == 5:
            return True
        else:
            print("Opção invalida, tente novamente.")


def cadastro_cliente():
    print("1 - Módulo Cadastro de Clientes - Informe os dados do cliente:")
    cliente = {
        "nome": formata_texto(input("Nome: ")),
        "cpf": valida_cpf(),
        "rg": valida_rg(),
        "data_nascimento": valida_data_nascimento(),
        "endereco": cadastro_endereco(),
    }
    retornar_menu(cliente, cadastro_cliente)
    clientes.append(cliente)


def cadastro_acao():
    print("2 - Módulo Cadastro de Ações - Informe os dados da ação:")
    acao = {
        "nome": input("Nome: "),
        "ticket": input("Ticket: "),
        "valor_compra": float(input("Valor de compra: ")),
        "quantidade_compra": int(input("Quantiodade: ")),
        "data_compra": valida_data_compra()
    }
    retornar_menu(acao, cadastro_acao)
    acoes.append(acao)


def analise():
    print("3 - Realizar análise da carteira")


def imprime_relatorio():
    print("4 - Imprimir relatório da carteira")


clientes = []
acoes = []


def main():
    menu_principal()


if __name__ == "__main__":
    main()
