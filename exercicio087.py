matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_numero = 0


for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o número na posição [{linha}][{coluna}].'))

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
                        
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

        if linha == 1 and matriz[linha][coluna] > maior_numero:
            maior_numero = matriz[linha][coluna]

print('-=' * 30)

for linha in range (0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')

print('-=' * 30)
print(f'A soma dos pares é igual a: {soma_pares}')
print(f'A soma da 3º coluna é igual a: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha: {maior_numero}')
