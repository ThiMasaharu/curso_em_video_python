from time import sleep

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro: '))

i = 0
while i != 5:
    print('Opções do programa'.center(40, '='))
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    print('='*38)
    i = int(input('Qual opção você deseja? '))
    if i == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1+n2:.2f}.')
        sleep(4)
    elif i == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a {n1*n2:.2f}.')
        sleep(4)
    elif i == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
            sleep(4)
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
            sleep(4)
        else:
            print(f'{n1} e {n2} são iguais.')
            sleep(4)
    elif i == 4:
        n1 = float(input('Digite o primeiro novo valor: '))
        n2 = float(input('Digite o segundo novo valor: '))
        sleep(2)
    elif i == 5:
        print('...')
        sleep(1)
        print('Programa finalizado. Até a próxima.')
    else:
        print('Opção inválida. Tente novamente.')
        sleep(3)   
