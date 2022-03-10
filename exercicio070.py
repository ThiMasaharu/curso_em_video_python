total_preco = total_mais1000 = menor_preco = i = 0
produto_mais_barato = ''

print(' Mercado bacana '.center(40, '='))

while True:
    produto = str(input('Qual produto comprou? '))
    preco = float(input('Qual foi o preço? '))
    total_preco += preco
    i += 1

    if preco > 1000:
        total_mais1000 += 1
    
    if i == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    opcao_continua = str(input('Deseja continuar? [S/N] ')).strip()[0]

    while opcao_continua not in 'SsNn':
        opcao_continua = str(input('Opção inválida. Tente novamente. [S/N] ')).strip()[0]

    print('-' * 40)

    if opcao_continua in 'Nn':
        print('Programa encerrado.')
        print(f'Total gasto: R${total_preco:.2f}.')
        print(f'Total de produtos com mais de R$1000,00: {total_mais1000}.')
        print(f'Produto mais barato, custando R${menor_preco:.2f}: {produto_mais_barato}')   
