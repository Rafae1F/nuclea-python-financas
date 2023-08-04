from models import ordem
from models.cliente import Cliente
from repository.banco_de_dados import conexao
from utils.cep import cadastro_endereco
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import *
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


def menu_cliente():
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
            cpf_consulta = input("Digite o CPF do cliente a ser consultado: ")
            consulta_cliente = Cliente()
            consulta_cliente.consultar_cliente(cpf_consulta)
        elif opcao == 3:
            cpf_atualizacao = input("Digite o CPF do cliente a ser atualizado: ")
            consulta_cliente = Cliente()
            cliente = consulta_cliente.consultar_cliente(cpf_atualizacao)
            if cliente:
                cliente.nome = input("Digite o novo nome do cliente: ")
                cliente.cpf = valida_cpf()
                cliente.rg = valida_rg()
                cliente.data_nascimento = valida_data_nascimento()
                cliente.endereco = cadastro_endereco()
                consulta_cliente.alterar_cliente()
                print("Cliente atualizado com sucesso!")
            else:
                print("Cliente não encontrado.")
        elif opcao == 4:
            cpf_delecao = input("Digite o CPF do cliente a ser deletado: ")
            conditions = {'cpf': cpf_delecao}
            if conexao.select_cliente_banco_de_dados(conditions):
                conexao.delete_cliente_banco_de_dados(cpf_delecao)
                print("Cliente deletado com sucesso!")
            else:
                print("Cliente não encontrado.")
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
        "data_nascimento": valida_data_nascimento()
    }
    retornar_menu(cliente, cadastro_cliente)
    cliente['endereco'] = cadastro_endereco()
    print(cliente)
    novo_cliente = Cliente()
    novo_cliente.cadastrar_cliente(cliente)
    clientes.append(cliente)
    print("Cadastro finalizado com sucesso!")


def menu_ordem():
    print("2 - Módulo Cadastro - Ordem de Ações - Informe seu cpf para acessar o sistema: ")
    cpf_consulta = input("CPF: ")
    conditions = {'cpf': cpf_consulta}
    cliente_selecionado = conexao.select_cliente_banco_de_dados(conditions)
    if cliente_selecionado:
        ordem.Ordem.cadastrar_ordem(cliente_selecionado)
        retornar_menu(cliente_selecionado, menu_ordem())
        print("Ordem finalizada com sucesso!")
    else:
        print("Documento não encontrado.")


def analise():
    print("3 - Realizar análise da carteira")


def imprime_relatorio():
    print("4 - Imprimir relatório da carteira")


clientes = []
ordens = []


def main():
    print("Seja bem-vindo(a) ao Sistema de Gerenciamento de Carteira de Ações da Nuclea. "
          "Selecione uma das opções abaixo:")
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
            menu_cliente()
        elif opcao == 2:
            menu_ordem()
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


if __name__ == "__main__":
    main()
