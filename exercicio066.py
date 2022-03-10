soma = quantidade = 0

while True:
    valor = int(input('Digite um número para somar (999 para parar): '))

    if valor == 999:
        break
    
    soma += valor
    quantidade += 1

print(f'A soma dos {quantidade} valores foi {soma}')