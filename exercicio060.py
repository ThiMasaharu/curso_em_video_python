fatorial = int(input('Digite um número para calcular o fatorial: '))
i = fatorial
f = 1

print(f'Calculando {fatorial}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1

print(f)
