import re
import yfinance as yf


def valida_ticker():
    while True:
        ticker = input("Digite o ticket da ação: ").strip().upper()
        padrao = re.compile(r'^[A-Z]+[0-9]*$')
        if padrao.match(ticker):
            try:
                acao = yf.Ticker(ticker + '.SA')
                acao_info = acao.info
                print(acao_info)
                if acao_info is not None:
                    return ticker
                else:
                    print("Ticker inválido ou não encontrado.")
            except:
                print("Ticker inválido ou não encontrado.")
        else:
            print("Ticker inválido")
