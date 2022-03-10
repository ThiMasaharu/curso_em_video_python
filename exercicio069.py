mais_18 = homem = mulher_menos_20 = 0

print(' Cadastro de pessoas '.center(40, '='))

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F] ')).strip()[0]

    while sexo not in 'MmFf':
        sexo = str(input('Sexo inválido. Tente novamente [M/F] ')).strip()[0]
    
    print('-' * 20)

    if idade > 18:
        mais_18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1
    
    opcao_continua = str(input('Deseja continuar? [S/N]')).strip()[0]

    while opcao_continua not in 'SsNn':
        opcao_continua = str(input('Opção inválida. Tente novamente. [S/N]'))
    
    if opcao_continua in 'Nn':
        print('Programa encerrado.')
        print(f'{mais_18} pessoas com mais de 18 anos.')
        print(f'{homem} homens cadastrados.')
        print(f'{mulher_menos_20} mulheres com menos de 20 anos.')
        print('-' * 20)
        break
