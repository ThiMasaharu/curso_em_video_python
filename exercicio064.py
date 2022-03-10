soma = quantidade = 0

valor = int(input('Digite um número a ser somado [999 para parar]: '))
while valor != 999:
    soma += valor
    quantidade += 1
    valor = int(input('Digite um número a ser somado [999 para parar]: '))

print(f'Você digitou {quantidade} números e a soma deles deu {soma}')
