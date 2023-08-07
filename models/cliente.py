from repository.banco_de_dados import BancoDeDados
from utils.cep import cadastro_endereco
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto, retornar_menu
from utils.valida_cpf import valida_cpf
from utils.valida_nome import valida_nome
from utils.valida_rg import valida_rg


clientes = []


class Cliente:
    def __init__(self):
        self.id = None
        self.nome = None
        self.cpf = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.numero_residencia = None
        self.complemento = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.ddd = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_cliente(self, cliente):
        self.id = "id"
        self.nome = "nome"
        self.cpf = "cpf"
        self.rg = "rg"
        self.data_nascimento = "data_nascimento"
        self.cep = "cep"
        self.logradouro = "logradouro"
        self.numero_residencia = "numero_residencia"
        self.complemento = "complemento"
        self.bairro = "bairro"
        self.cidade = "cidade"
        self.estado = "estado"
        self.ddd = "ddd"
        self.banco_de_dados.insert_cliente_banco_de_dados(cliente)

    def consultar_cliente(self, cpf):
        cliente_selecionado = self.banco_de_dados.select_cliente_banco_de_dados(cpf)
        return cliente_selecionado

    def alterar_cliente(self, cpf, novos_dados):
        self.banco_de_dados.update_cliente_banco_de_dados(cpf, novos_dados)

    def delete_cliente(self, cpf):
        self.banco_de_dados.delete_cliente_banco_de_dados(cpf)

    def cadastro_cliente(self):
        print("[1] - Módulo Cadastro de Clientes - Informe os dados do cliente:")
        cliente = {
            "nome": formata_texto(valida_nome()),
            "cpf": valida_cpf(),
            "rg": valida_rg(),
            "data_nascimento": valida_data_nascimento()
        }
        retornar_menu(cliente, self.cadastro_cliente)
        cliente['endereco'] = cadastro_endereco()
        self.cadastrar_cliente(cliente)
        clientes.append(cliente)
        print(cliente)
        print("Cadastro finalizado com sucesso!")

    def consulta_cliente(self):
        cpf_consulta = input("Digite o CPF do cliente a ser selecionado: ")
        cliente_selecionado = self.consultar_cliente(cpf_consulta)
        if cliente_selecionado is not None:
            print("Cliente encontrado!")
            return cpf_consulta, self
        else:
            print("Documento não encontrado na base de dados")

    def atualiza_cliente(self):
        cpf_consulta = input("Digite o CPF do cliente a ser atualizado: ")
        cliente_encontrado = self.consultar_cliente(cpf_consulta)
        if cliente_encontrado is not None:
            print("Informe os dados a serem atualizados: ")
            novos_dados = {
                'nome': formata_texto(input("Nome: ")),
                'cpf': valida_cpf(),
                'rg': valida_rg(),
                'data_nascimento': valida_data_nascimento(),
                'endereco': cadastro_endereco()
            }
            self.alterar_cliente(cpf_consulta, novos_dados)
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def deleta_cliente(self):
        cpf_consulta = input("Digite o CPF do cliente a ser deletado: ")
        cliente_encontrado = self.consultar_cliente(cpf_consulta)
        if cliente_encontrado is not None:
            confirmacao = input("Tem certeza que deseja remover esse cliente? (sim/nao) ")
            if confirmacao in ["sim", "s"]:
                self.delete_cliente(cpf_consulta)
                print("Cliente deletado com sucesso!")
            elif confirmacao in ["nao", "n"]:
                return True
            else:
                print("Opção inválida!")
        else:
            print("Documento não encontrado na base de dados")
