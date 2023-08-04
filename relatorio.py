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


if __name__ == "__main__":
    # Solicitar ao usuário o código da ação e o nome do arquivo
    ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

    # Obter e mostrar os dados da ação e exportar para o arquivo
    obter_dados_acao(ticket, nome_arquivo)
