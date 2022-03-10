soma = 0
contador = 0

for i in range(0,6):
    valor = int(input('Digite um número a ser somado: '))
    if valor % 2 == 0:
        soma += valor
        contador += 1
print('Você informou {} números pares e é igual a {}'.format(contador, soma))
