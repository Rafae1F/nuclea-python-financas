from repository.banco_de_dados import BancoDeDados

clientes = []


class Cliente:
    def __init__(self):
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

    def consultar_cliente(self, consulta):
        condicao = {'cpf': consulta}
        self.banco_de_dados.select_cliente_banco_de_dados(condicao)

    def alterar_cliente(self):
        condicao = {'cpf': self}
        self.banco_de_dados.update_cliente_banco_de_dados(condicao)

    def delete_cliente(self, cpf_delecao):
        self.banco_de_dados.delete_cliente_banco_de_dados(cpf_delecao)
