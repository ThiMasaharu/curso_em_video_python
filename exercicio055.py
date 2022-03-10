maior = 0
menor = 0

print('Digite o peso 5 vezes')
for pessoas in range (0, 5):
    peso = float(input('Peso: '))
    if pessoas == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O menor peso foi {}'.format(menor))
print('O maior peso foi {}'.format(maior))