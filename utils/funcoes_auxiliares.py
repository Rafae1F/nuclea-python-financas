def retornar_menu_principal():
    while True:
        retornar_menu_principal = input("Deseja retornar ao menu principal? ((s)im ou (n)ão): ").lower()
        if retornar_menu_principal in ["sim", "s"]:
            retorna_menu = True
        elif retornar_menu_principal in ["nao", "n"]:
            retorna_menu = False
        else:
            print("Opção inválida, tente novamente. Digite 'sim' ou 'não'.")
        return retorna_menu


def retornar_menu(item_cadastro, campo_cadastro):
    while True:
        for item in item_cadastro:
            if isinstance(item_cadastro[item], dict):
                pass
            else:
                print("{0:20} {1:20}".format(item, (item_cadastro[item])))

        retornar_menu = input(f"Os dados acima estão corretos? Digite (s)im ou (n)ão ").lower()
        if retornar_menu in ["sim", "s"]:
            print("Cadastro efetuado com sucesso!")
            return item_cadastro
        elif retornar_menu in ["nao", "n"]:
            print("Refazer cadastro")
            return campo_cadastro()
        else:
            print("Opção inválida, tente novamente.")


def sair():
    print("Sair")
    print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
    exit()


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado
