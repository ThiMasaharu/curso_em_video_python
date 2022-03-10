soma = 0
quantidadeImparMultiploDeTres = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        quantidadeImparMultiploDeTres += 1
print('A soma dos {} números ímpares múltiplos de 3 é igual a {}'.format(quantidadeImparMultiploDeTres, soma))
