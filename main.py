import models.cliente
import models.ordem
from utils.funcoes_auxiliares import retornar_menu_principal


def main():
    print("Seja bem-vindo(a) ao Sistema de Gerenciamento de Carteira de Ações da Nuclea. "
          "Selecione uma das opções abaixo:")
    validador = True
    while validador:
        print("=============== MENU ===============")
        print("[1] - Cliente")
        print("[2] - Cadastrar ação")
        print("[3] - Realizar análise da carteira")
        print("[4] - Imprimir relatório de ações")
        print("[5] - Sair")

        opcao = input("Escolha uma opção de 1 a 5: ")

        cliente = models.cliente.Cliente()
        ordem = models.ordem.Ordem()

        if opcao == "1":
            print("=========== MENU CLIENTE ===========")
            print("[1] - Cadastrar cliente")
            print("[2] - Consultar cliente")
            print("[3] - Atualizar cliente")
            print("[4] - Deletar cliente")
            print("[5] - Retornar ao menu principal")

            opcao = input("Escolha uma opção de 1 a 5: ")

            if opcao == "1":
                cliente.cadastro_cliente()
            elif opcao == "2":
                cliente.consulta_cliente()
            elif opcao == "3":
                cliente.atualiza_cliente()
            elif opcao == "4":
                cliente.deleta_cliente()
            elif opcao == "5":
                validador = retornar_menu_principal()
            else:
                print("Opção invalida, tente novamente.")
        elif opcao == "2":
            ordem.cadastro_ordem(cliente)
        elif opcao == "3":
            ordem.analise_carteira(cliente)
        elif opcao == "4":
            print("====== MENU RELATÓRIO CARTEIRA ======")
            print("[1] - Imprimir relatório da carteira")
            print("[2] - Consultar relatório da ação")
            print("[3] - Retornar ao menu principal")

            opcao = input("Escolha uma opção de 1 a 3: ")

            if opcao == "1":
                ordem.imprime_relatorio_carteira(cliente)
            elif opcao == "2":
                ordem.imprime_relatorio()
            elif opcao == "3":
                validador = retornar_menu_principal()
            else:
                print("Opção inválida!")
        elif opcao == "5":
            print("Sair")
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida, tente novamente. Escolha uma opção entre 1 e 5.")


if __name__ == "__main__":
    main()
