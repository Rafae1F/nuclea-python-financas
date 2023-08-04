class Ordem:
    def __init__(self):
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None

    def cadastrar_ordem(self, cliente):
        self.id_cliente = cliente
