from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numero_sorteado = randint(1, 10)
        lista.append(numero_sorteado)
        print(f'{lista[i]}', end=' ', flush=True)
        sleep(0.3)
    print('Pronto!')

def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}.')

lista_numeros_sorteados = []
sorteia(lista_numeros_sorteados)
soma_par(lista_numeros_sorteados)
