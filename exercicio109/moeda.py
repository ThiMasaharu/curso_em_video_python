def aumentar(n = 0, t = 0, formato = False):
    calculo = n + (t/100 * n)
    return calculo if formato is False else moeda(calculo)

def diminuir(n = 0, t = 0, formato = False):
    calculo = n - (t/100 * n)
    return calculo if formato is False else moeda(calculo)

def dobro(n = 0, formato = False):
    calculo = n * 2
    return calculo if formato is False else moeda(calculo)

def metade(n = 0, formato = False):
    calculo = n / 2
    return calculo if formato is False else moeda(calculo)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.' , ',')