n1 = int(input('Digite um inteiro: '))
n2 = int(input('Digite outro inteiro: '))

if n1>n2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(n1, n2))
elif n1<n2:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(n2, n1))
else:
    print('Os primeiro valor {} e segundo valor {} são iguais'.format(n1, n2))
