from random import randint
from time import sleep

lista_jogadas = []
lista_jogo = []
print('-=' * 30)
quantidade_jogadas = int(input('Quantas jogadas deseja sortear? '))
print('-=' * 30)
print(f'{"Jogadas mega sena":^40}')

for jogada in range (0, quantidade_jogadas):
    contador = 0
    while True:
        numero_aleatorio = randint(1, 60)
        
        if numero_aleatorio not in lista_jogo:
            lista_jogo.append(numero_aleatorio)
            contador += 1

        if contador == 6:
            lista_jogo.sort()
            break
    lista_jogadas.append(lista_jogo[:])
    lista_jogo.clear()
    print(f'{jogada+1}ª jogada: {lista_jogadas[jogada]}')
    sleep(1)

print('Boa sorte.')
