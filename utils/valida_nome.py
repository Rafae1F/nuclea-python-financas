def valida_nome():
    while True:
        nome = input("Nome: ")
        if len(nome) > 2:
            return nome
        else:
            print("O nome não pode estar em branco e deve ter no mínimo 3 caracteres")
