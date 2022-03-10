lista_dados = []
lista_pessoas = []
menor_peso = maior_peso = 0

while True:
    lista_dados.append(str(input('Digite o nome: ')))
    lista_dados.append(float(input('Digite o peso: ')))
    if len(lista_pessoas) == 0:
        menor_peso = maior_peso = lista_dados[1]
    else:
        if lista_dados[1] > maior_peso:
            maior_peso = lista_dados[1]
        
        if lista_dados[1] < menor_peso:
            menor_peso = lista_dados[1]
           
    lista_pessoas.append(lista_dados[:])
    lista_dados.clear()

    resposta = str(input('Quer continuar? [S/N]' )).strip()[0]

    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida. Tente novamente [S/N]. ')).strip()[0]

    if resposta in 'Nn':
        print(f'{lista_pessoas}')
        print(f'Total de pessoas cadastradas: {len(lista_pessoas)}.')
        print(f'Pessoas mais pesadas, pesando {maior_peso} kg: ', end='')
        
        for pessoas in lista_pessoas:
            if pessoas[1] == maior_peso:
                print(f'{pessoas[0]} ', end='')
        
        print('')
        print(f'Pessoas de menor peso, pesando {menor_peso} kg: ', end='')
        for pessoas in lista_pessoas:
            if pessoas[1] == menor_peso:
                print(f'{pessoas[0]} ', end='')
        
        break
