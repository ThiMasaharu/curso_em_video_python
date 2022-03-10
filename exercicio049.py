numero = int(input('Digite o número da tabuada desejada: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(numero, i, numero*i))
