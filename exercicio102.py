def fatorial(n, show=False):
    """
    fatorial(n, show=False)
    -> Calcula o fatorial de um número (n).
    :parâmetro n: Fatorial a ser calculado.
    :parâmetro show: (Opcional) Mostra ou não a conta (False mostra. True não mostra.).
    :return: O resultado da fatorial de (n).
    """
    print('-' * 30)
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show == False:
            print(f'{i} x ', end='') if i!= 1 else print(f'{i} = ', end='')
    return f
        
print(fatorial(3, True))
print(fatorial(5, False))
print(fatorial(7))
# help(fatorial)
    