tupla = (int(input('Digite um valor: ')),
    int(input('Segundo valor: ')),
    int(input('Terceiro valor: ')),
    int(input('Quarto valor: ')))

print(f'Números digitados: {tupla}')

print(f'Número de vezes que o 9 apareceu: {tupla.count(9)}.')

if 3 in tupla:
    print(f'O valor 3 apareceu pela primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

print('Valores pares digitados: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}', end=', ')
print('Fim.')