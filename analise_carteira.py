import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def analise_carteira_cliente(carteira, data_inicio, data_fim):
    # Definir o período de data desejado
    start_date = data_inicio
    end_date = data_fim

    chave_desejada = 'ticket'
    lista = [dado[chave_desejada] for dado in carteira]

    # Criar um DataFrame vazio
    df = pd.DataFrame()

    # Baixar os dados para cada ação e adicionar ao DataFrame
    for i in lista:
        cotacao = yf.download(i + '.SA', start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    # Plotar as séries de preços do DataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()
