lista_numeros = [[], []]

for i in range (1, 8):
    valor_digitado = int(input(f'Digite o {i}º número.'))

    if valor_digitado % 2 == 0:
        lista_numeros[0].append(valor_digitado)
    else:
        lista_numeros[1].append(valor_digitado)

lista_numeros[0].sort()
lista_numeros[1].sort()
print(f'Os números pares digitados foram: {lista_numeros[0]}')
print(f'Os números ímpares digitados foram: {lista_numeros[1]}')
