while True:
    print('Gerador de tabuada'.center(40, '='))
    tabuada = int(input('Digite um número para fazer a tabuada: '))
    
    if tabuada < 0:
        break

    for i in range (1, 11):
        print(f'{tabuada} x {i} = {tabuada*i}')
    
print('Programa encerrado. Volte sempre.')
