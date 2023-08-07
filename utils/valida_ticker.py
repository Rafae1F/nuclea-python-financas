import re


def valida_ticker():
    while True:
        ticker = input("Digite o ticket da ação: ").strip().upper()

        padrao = re.compile(r'^[A-Z]+[0-9]*$')

        if padrao.match(ticker):
            return ticker
        else:
            print("Ticker inválido")
