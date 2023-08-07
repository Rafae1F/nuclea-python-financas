from analise_carteira import analise_carteira_cliente
from relatorio import obter_dados_acao, obter_dados_carteira_cliente
from repository.banco_de_dados import BancoDeDados
from utils.data import valida_data_compra, valida_data_inicio, valida_data_fim, converte_data_alt
from utils.funcoes_auxiliares import retornar_menu
from utils.valida_ticker import valida_ticker

ordens = []


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

    def cadastro_ordem(self, cliente):
        print("[2] - Módulo Cadastro de Ordem/Ações - Informe seu cpf para acessar o sistema: ")
        cpf = input("CPF: ")
        cliente_encontrado = cliente.consultar_cliente(cpf)
        if cliente_encontrado is not None:
            ordem = {
                'nome': input("Digite o nome da ação: ").upper(),
                'ticket': valida_ticker(),
                'valor_compra': float(input("Digite o valor de compra: ")),
                'quantidade_compra': int(input("Digite a quantidade: ")),
                'data_compra': valida_data_compra(),
                'cliente_id': cliente_encontrado['id']
            }
            retornar_menu(ordem, self.cadastro_ordem)
            self.cadastrar_ordem(ordem)
            ordens.append(ordem)
            print("Ordem finalizada com sucesso!")
        else:
            print("Documento não encontrado.")

    def analise_carteira(self, cliente):
        print("[3] - Realizar análise da Carteira - Cliente")
        cpf = input("Informe o CPF para consultar a carteira: ")
        cliente_encontrado = cliente.consultar_cliente(cpf)
        if cliente_encontrado is not None:
            consulta_carteira = self.consultar_ordem(cliente_encontrado['id'])
            if consulta_carteira is not None:
                data_inicio = valida_data_inicio()
                data_fim = valida_data_fim(data_inicio)
                data_inicio = converte_data_alt(data_inicio)
                data_fim = converte_data_alt(data_fim)
                analise_carteira_cliente(consulta_carteira, data_inicio, data_fim)
            else:
                print("Não existem ações vinculadas a esse documento.")
        else:
            print("Documento não encontrado na base de dados.")

    def imprime_relatorio_carteira(self, cliente):
        print("[1] - Imprimir relatório da carteira")
        cpf_consulta = input("Informe o CPF para consultar a carteira: ")
        cliente_encontrado = cliente.consultar_cliente(cpf_consulta)
        if cliente_encontrado is not None:
            consulta_carteira = self.consultar_ordem(cliente_encontrado['id'])
            if consulta_carteira is not None:
                nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
                obter_dados_carteira_cliente(consulta_carteira, nome_arquivo)
            else:
                print("Não existem ações vinculadas a esse documento.")
        else:
            print("Documento não encontrado na base de dados.")

    @staticmethod
    def imprime_relatorio():
        print("[2] - Imprimir relatório da carteira")
        ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
        obter_dados_acao(ticket, nome_arquivo)
