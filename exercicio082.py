lista_inteira = []
lista_par = []
lista_impar = []

while True:
    valor_a_adicionar = int(input('Digite um número: '))
    lista_inteira.append(valor_a_adicionar)

    if valor_a_adicionar % 2 == 0:
        lista_par.append(valor_a_adicionar)
    else:
        lista_impar.append(valor_a_adicionar)
    
    resposta = str(input('Deseja continuar? [S/N]')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida. Tente novamente. [S/N]')).strip()[0]
    
    if resposta in 'Nn':
        print(f'A lista completa é {lista_inteira}.')
        print(f'A lista de pares é {lista_par}')
        print(f'A lista de ímpares é {lista_impar}')
        print(f'Programa encerrado. Volte sempre.')
        break
