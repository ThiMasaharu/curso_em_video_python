lista = []

while True:
    valor = (int(input('Digite um valor: ')))
    
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = str(input('Deseja continuar? ')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida. Tente novamente. ')).strip()[0]

    if resposta in 'Nn':
        break

print('-=' * 20)
lista.sort()
print(f'{lista}')
