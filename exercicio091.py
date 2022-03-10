from random import randint
from time import sleep
from operator import itemgetter

ranking = {}
jogador = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6)}

print('Valores sorteados:')
for i, j in jogador.items():
    print(f'{i} tirou {j} no dado.')
    sleep(1)

ranking = sorted(jogador.items(),key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print(f'Em {i+1}º lugar: {j[0]} com {j[1]}.')
