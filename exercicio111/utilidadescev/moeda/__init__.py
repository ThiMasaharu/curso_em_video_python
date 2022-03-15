def aumentar(n = 0, t = 0, formato = False):
    """
    -> programa para aumentar o preço, conforme taxa.
    :param n: preço informado
    :param t: taxa informada
    :param formato: se será formatado ou não
    :return: reajuste do valor, formatado ou não
    """
    calculo = n + (t/100 * n)
    return calculo if formato is False else moeda(calculo)

def diminuir(n = 0, t = 0, formato = False):
    '''
    -> programa para diminuir o preço, conforme taxa.
    :param n: preço informado
    :param t: taxa informada
    :param formato: se o resultado será formatado ou não
    :return: reajuste do valor, formatado ou não
    '''
    calculo = n - (t/100 * n)
    return calculo if formato is False else moeda(calculo)

def dobro(n = 0, formato = False):
    """
    -> programa para dobrar o preço.
    :param n: preço informado.
    :formato: se o resultado será formatado ou não.
    :return: reajuste do valor, formatado ou não.
    """
    calculo = n * 2
    return calculo if formato is False else moeda(calculo)

def metade(n = 0, formato = False):
    """
    -> programa para dividir o preço pela metade.
    :param n: preço informado.
    :formato: se o resultado será formatado ou não.
    :return: reajuste do valor, formatado ou não.
    """
    calculo = n / 2
    return calculo if formato is False else moeda(calculo)

def moeda(n = 0, moeda = 'R$'):
    '''
    -> Função para formatar a moeda
    :param n: preço informado.
    :param moeda: informar a moeda(caso não informe será Real).
    :return: formatação do valor.
    '''
    return f'{moeda}{n:.2f}'.replace('.' , ',')

def resumo(n=0, aumento=0, reducao=0):
    """
    -> Função que mostra em forma de tabela análises do preço.
    :param n: preço informado.
    :param aumento: taxa de aumento informado.
    :param reducao: taxa de redução informado.
    :return: retorna tabela com valor, dobro, metade, aumento e redução do preço.
    """
    print('-'*40)
    print('Resumo do valor'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(n)}.')
    print(f'Dobro do preço: \t{dobro(n, True)}.')
    print(f'Metade do preço: \t{metade(n, True)}.')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}.')
    print(f'{reducao}% de redução: \t{diminuir(n, reducao, True)}.')
    print('-'*40)