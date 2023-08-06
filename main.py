from analise_carteira import analise_carteira_cliente
from models.cliente import Cliente
from models.ordem import Ordem
from relatorio import obter_dados_acao
from utils.cep import cadastro_endereco
from utils.data import valida_data_nascimento, valida_data_compra, valida_data_fim, valida_data_inicio, \
    converte_data_alt
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
            consulta_cliente()
        elif opcao == 3:
            atualiza_cliente()
        elif opcao == 4:
            deleta_cliente()
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
    novo_cliente = Cliente()
    novo_cliente.cadastrar_cliente(cliente)
    clientes.append(cliente)
    print(cliente)
    print("Cadastro finalizado com sucesso!")


def consulta_cliente():
    cliente = Cliente()
    cpf_consulta = input("Digite o CPF do cliente a ser selecionado: ")
    cliente_selecionado = cliente.consultar_cliente(cpf_consulta)
    if cliente_selecionado is not None:
        print("Cliente encontrado!")
        return cpf_consulta, cliente
    else:
        print("Documento não encontrado na base de dados")


def atualiza_cliente():
    cliente = Cliente()
    cpf_consulta = input("Digite o CPF do cliente a ser atualizado: ")
    cliente_encontrado = cliente.consultar_cliente(cpf_consulta)
    if cliente_encontrado is not None:
        print("Informe os dados a serem atualizados: ")
        novos_dados = {
            'nome': formata_texto(input("Nome: ")),
            'cpf': valida_cpf(),
            'rg': valida_rg(),
            'data_nascimento': valida_data_nascimento(),
            'endereco': cadastro_endereco()
        }
        cliente.alterar_cliente(cpf_consulta, novos_dados)
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")


def deleta_cliente():
    cliente = Cliente()
    cpf_consulta = input("Digite o CPF do cliente a ser deletado: ")
    cliente_encontrado = cliente.consultar_cliente(cpf_consulta)
    if cliente_encontrado is not None:
        confirmacao = input("Tem certeza que deseja remover esse cliente? (sim/nao) ")
        if confirmacao in ["sim", "s"]:
            cliente.delete_cliente(cpf_consulta)
            print("Cliente deletado com sucesso!")
        elif confirmacao in ["nao", "n"]:
            return True
        else:
            print("Opção inválida!")
    else:
        print("Documento não encontrado na base de dados")


def cadastro_ordem():
    cliente = Cliente()
    nova_ordem = Ordem()
    print("2 - Módulo Cadastro de Ordem/Ações - Informe seu cpf para acessar o sistema: ")
    cpf = input("CPF: ")
    cliente_encontrado = cliente.consultar_cliente(cpf)
    if cliente_encontrado is not None:
        ordem = {
            'nome': input("Digite o nome da ação: ").upper(),
            'ticket': input("Digite o ticket da ação: ").strip().upper(),
            'valor_compra': float(input("Digite o valor de compra: ")),
            'quantidade_compra': int(input("Digite a quantidade: ")),
            'data_compra': valida_data_compra(),
            'cliente_id': cliente_encontrado['id']
        }
        retornar_menu(ordem, cadastro_ordem)
        nova_ordem.cadastrar_ordem(ordem)
        ordens.append(ordem)
        print("Ordem finalizada com sucesso!")
    else:
        print("Documento não encontrado.")


def menu_analise():
    while True:
        print("=========== MENU CLIENTE ===========")
        print("1 - Fazer analise da carteira cliente")
        print("2 - Consultar ações")
        print("3 - Retornar ao menu principal")
        opcao = int(input("Escolha uma opção de 1 a 5: "))
        if opcao == 1:
            analise_carteira()
        elif opcao == 2:
            consulta_acoes = input("Informe os tickets para analise: ex: BBAS3, BRFS3 ")
            data_inicio = valida_data_inicio()
            data_fim = valida_data_fim(data_inicio)
            analise_carteira_cliente(consulta_acoes, data_inicio, data_fim)
        elif opcao == 3:
            return True
        else:
            print("Opção inválida!")


def analise_carteira():
    print("1 - Realizar análise da Carteira - Cliente")
    cliente = Cliente()
    carteira = Ordem()
    cpf_consulta = input("Informe o CPF para consultar a carteira: ")
    cliente_encontrado = cliente.consultar_cliente(cpf_consulta)
    if cliente_encontrado is not None:
        data_inicio = valida_data_inicio()
        data_fim = valida_data_fim(data_inicio)
        data_inicio = converte_data_alt(data_inicio)
        data_fim = converte_data_alt(data_fim)
        consulta_carteira = carteira.consultar_ordem(cliente_encontrado['id'])
        analise_carteira_cliente(consulta_carteira, data_inicio, data_fim)
    else:
        print("Documento não encontrado na base de dados.")


def imprime_relatorio():
    print("4 - Imprimir relatório da carteira")
    ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
    obter_dados_acao(ticket, nome_arquivo)


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
            cadastro_ordem()
        elif opcao == 3:
            menu_analise()
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
