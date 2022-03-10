from random import randint

print('Pensei em um número... consegue adivinhar?')

computador = randint(0,10)
jogador = int(input('Qual número eu pensei? '))
tentativas = 1

while jogador != computador:
    tentativas += 1

    if jogador > computador:
        jogador = int(input('Tente um número menor: '))
    else:
        jogador = int(input('tente um número maior: '))

print('Parabéns! Pensei no número {} e você acertou em {} tentativas.'.format(computador, tentativas))