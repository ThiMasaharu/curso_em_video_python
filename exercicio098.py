from time import sleep

def linha():
    print('-=' * 20)

def imprime_exemplos_contadores():
    linha()
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('FIM!')
    linha()
    print('Contagem de 10 a 0 de 2 em 2:')
    for i in range(10, -1, -2):
        print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('FIM!')
    linha()
    print('Agora é sua vez de personalizar a contagem!')

def contador_personalizado(inicio, fim, passo):
    if inicio > fim:
        for i in range(inicio, fim - 1, passo):
            print(f'{i}', end=' ', flush=True)
            sleep(0.3)
        print('FIM!')
    else:
        for i in range(inicio, fim + 1, passo):
            print(f'{i}', end=' ', flush=True)
            sleep(0.3)
        print('FIM!')
    linha()    

imprime_exemplos_contadores()
inic = int(input('Início: '))
fin = int(input('Fim: '))
pas = int(input('Passo: '))
contador_personalizado(inic, fin, pas)
    