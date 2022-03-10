from random import randint
from time import sleep

print('''Opções de jogada:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogada = int(input('Qual a sua jogada? '))
jogadaComputador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if jogada == 0:
    if jogadaComputador == 0:
        print('Empate. Os dois jogaram pedra.')
    elif jogadaComputador == 1:
        print('Computador venceu por jogar papel.')
    elif jogadaComputador == 2:
        print('Você venceu. O computador jogou tesoura.')
    else:
        print('Jogada inválida.')
elif jogada == 1:
    if jogadaComputador == 0:
        print('Você venceu. O computador jogou pedra.')
    elif jogadaComputador == 1:
        print('Empate. Os dois jogaram papel.')
    elif jogadaComputador == 2:
        print('Você perdeu. O computador jogou tesoura')
    else:
        print('Jogada inválida.')
elif jogada == 2:
    if jogadaComputador == 0:
        print('Você perdeu. O computador jogou pedra.')
    elif jogadaComputador == 1:
        print('Você venceu. O computador jogou papel.')
    elif jogadaComputador:
        print('Empate. Os dois jogaram tesoura.')
    else:
        print('Jogada inválida.')
else:
    print('Jogada inválida.')
