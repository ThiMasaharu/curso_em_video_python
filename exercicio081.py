lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resposta = str(input('Deseja continuar? [S/N]')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida. Tente novamente. [S/N]')).strip()[0]
    
    if resposta in 'Nn':
        print('-=' * 30)
        print(f'Você digitou {len(lista)} elementos.')
        lista.sort(reverse = True)
        print(f'Os valores em ordem decrescente são: {lista}')

        if 5 in lista:
            print('O número 5 faz parte da lista.')
        else:
            print('O 5 não foi encontrado na lista.')

        print('Programa finalizado. Volte sempre.')
        break
