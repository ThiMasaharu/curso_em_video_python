numero = int(input('Digite um número: '))
quantidadeDivisivel = 0

for i in range(1, numero+1):
    if numero % i == 0:
        print('\033[33m', end='')
        quantidadeDivisivel += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')

if quantidadeDivisivel == 2:
    print('\n\033[mO número foi divisível 2 vezes, logo é primo.')
else:
    print('\n\033[mO número {} foi divisível {} vezes, logo não é primo.'.format(numero, quantidadeDivisivel))
