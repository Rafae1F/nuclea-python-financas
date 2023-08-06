import yfinance as yf


def obter_dados_acao(ticket, nome_arquivo):
    try:
        # Obter os dados da ação usando o Yahoo Finance (B3)
        acao = yf.download(ticket + '.SA', progress=False)

        # Exibir os dados
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatorio da acao: " + ticket + "\n")
            arquivo.write(str(acao.tail()))
            arquivo.close()

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")


def obter_dados_carteira_cliente(carteira, nome_arquivo):
    try:
        chave_desejada = 'ticket'
        lista = [dado[chave_desejada] for dado in carteira]
        with open(nome_arquivo + '.txt', 'w') as arquivo:
            for ticket in lista:
                acao = yf.download(ticket + '.SA', progress=False)
                if not acao.empty:
                    acao_info = carteira[lista.index(ticket)]
                    arquivo.write(f"Nome da Ação: {acao_info['nome']}\n")
                    arquivo.write(f"Ticket: {acao_info['ticket']}\n")
                    arquivo.write(f"Valor de compra:  {acao_info['valor_compra']} \n")
                    arquivo.write(f"Quantidade: {acao_info['quantidade_compra']}\n")
                    arquivo.write(f"Data da compra: {acao_info['data_compra']}\n")
                    arquivo.write(str(acao.tail()))
                    arquivo.write("\n\n")
            arquivo.close()
        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")
    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")


if __name__ == "__main__":
    # Solicitar ao usuário o código da ação e o nome do arquivo
    ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

    # Obter e mostrar os dados da ação e exportar para o arquivo
    obter_dados_acao(ticket, nome_arquivo)
