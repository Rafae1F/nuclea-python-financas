
def retornar_menu_principal():
    while True:
        opcao = input("Deseja retornar ao menu principal? ((s)im ou (n)ão): ").lower()
        if opcao in ["sim", "s"]:
            return True
        elif opcao in ["nao", "n"]:
            return False
        else:
            print("Opção inválida, tente novamente. Digite 'sim' ou 'não'.")


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


class Cliente:
    def __init__(self, nome, cpf, rg, data_nascimento, endereco):
            self.nome = nome
            self.cpf = cpf
            self.rg = rg
            self.data_nascimento = data_nascimento
            self. endereco = endereco


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado
