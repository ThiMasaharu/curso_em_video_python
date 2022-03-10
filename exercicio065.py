soma = quantidade = maior = menor = 0
opcao = str(input('Quer digitar um número [S/N]? ')).strip()[0]

while opcao in 'Ss':
    quantidade += 1
    valor = int(input('Digite um número: '))
    soma += valor

    if quantidade == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        
    opcao = str(input('Deseja continuar [S/N]? ')).strip()[0]

media = soma / quantidade

print(f'Você digitou {quantidade} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
