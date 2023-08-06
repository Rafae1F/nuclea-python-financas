from repository.banco_de_dados import conexao, BancoDeDados


class Ordem:
    def __init__(self):
        self.id = None
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_ordem(self, ordem):
        self.id = "id"
        self.nome = "nome"
        self.ticket = "ticket"
        self.valor_compra = "valor_compra"
        self.quantidade_compra = "quantidade_compra"
        self.data_compra = "data_compra"
        self.cliente_id = "cliente_id"
        self.banco_de_dados.insert_ordem_banco_de_dados(ordem)

    def consultar_ordem(self, cliente):
        carteira_selecionada = self.banco_de_dados.select_ordem_banco_de_dados(cliente)
        return carteira_selecionada
