from time import sleep


def maior(*valores):
    contador = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for i in valores:
        print(i, end=' ', flush = True)
        sleep(0.4)
        if contador == 0 or i > maior:
            maior = i
        contador += 1
    print(f'Foram informados {len(valores)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 20)

maior()