def aumentar(n = 0, t = 0):
    return n + (t/100 * n)

def diminuir(n = 0, t = 0):
    return n - (t/100 * n)

def dobro(n = 0):
    return n * 2

def metade(n = 0):
    return n / 2

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.' , ',')