from repository.banco_de_dados import conexao
from utils.data import valida_data_compra

ordens = []


class Ordem:
    def __init__(self):
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None

    def cadastrar_ordem(self, cliente_selecionado):
        self.nome: input("Nome: ")
        self.ticket: input("Ticket: ")
        self.valor_compra: float(input("Valor de compra: "))
        self.quantidade_compra: int(input("Quantidade: "))
        self.data_compra: valida_data_compra()
        self.cliente_id: cliente_selecionado
        conexao.insert_ordem_banco_de_dados(self)
        ordens.append(self)
        print(f"Nome: {self.nome} Ticket: {self.ticket} Valor de compra: {self.valor_compra} "
              f"Quantidade: {self.quantidade_compra} Data da compra: {self.data_compra}")
