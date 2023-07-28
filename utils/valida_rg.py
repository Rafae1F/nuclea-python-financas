import re


def valida_rg():
    while True:

        padrao_rg = r'(^\d{1,2}).?(\d{3}).?(\d{3})-?(\d{1}?|X?|x?$/,"$1.$2.$3-$4")'

        rg = input("RG: ")

        if re.match(padrao_rg, rg):
            return rg
        else:
            print("Tente novamente")


if __name__ == "__main__":
    valida_rg()
