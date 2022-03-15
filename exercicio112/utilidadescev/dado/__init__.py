def leia_dinheiro(entrada):
    validade = False
    while not validade:
        preco = input(entrada).replace(',','.').strip()
        if preco.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" não é um preço válido!\033[m')
        else:
            validade = True
            return float(preco)
