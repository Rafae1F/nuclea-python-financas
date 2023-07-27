def retornar_menu_principal():
    while True:
        retornar_menu_principal = input("Deseja retornar ao menu principal? ((s)im ou (n)ão): ").lower()
        if retornar_menu_principal in ["sim", "s"]:
            retorna_menu = True
        elif retornar_menu_principal in ["não", "nao", "n"]:
            retorna_menu = False
        else:
            print("Opção inválida, tente novamente. Digite 'sim' ou 'não'.")
        return retorna_menu


def sair():
    print("5 - Sair")
    print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
    exit()


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado
