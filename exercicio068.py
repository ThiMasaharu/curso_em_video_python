from random import randint

vitoria = 0

print('-='*20)
print('PAR OU ÍMPAR')
print('-='*20)

while True:
    jogada_jogador = int(input('Digite um número: '))
    escolha_jogador = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    jogada_computador = randint(0, 10)
    soma = jogada_jogador + jogada_computador

    while escolha_jogador not in 'PpIi':
        escolha_jogador = str(input('Escolha inválida. Tente novamente [P/I] ')).strip()[0]
    
    if escolha_jogador in 'Pp' and soma % 2 == 0:
        vitoria += 1
        print('-' * 40)
        print(f'Você jogou {jogada_jogador} e o computador {jogada_computador}. ', end='')
        print(f'O total deu {soma} e foi par.')
        print('Você venceu. Vamos jogar novamente.')
        print('-' * 40)
    elif escolha_jogador in 'Ii' and soma % 2 != 0:
        vitoria += 1
        print('-' * 40)
        print(f'Você jogou {jogada_jogador} e o computador {jogada_computador}. ', end='')
        print(f'O total deu {soma} e foi ímpar.')
        print('Você venceu. Vamos jogar novamente.')
        print('-' * 40)
    else:
        if soma % 2 == 0:
            print('-' * 40)
            print('GAME OVER! Você perdeu. Jogo encerrado.')
            print(f'Você jogou {jogada_jogador} e o computador {jogada_computador}. ', end='')
            print(f'O total deu {soma} e foi par.')
            print(f'Você obteu {vitoria} ', end='')
            print('vitória.' if vitoria == 1 else 'vitórias.')
            print('-' * 40)
        else:
            print('-' * 40)
            print('GAME OVER! Você perdeu. Jogo encerrado.')
            print(f'Você jogou {jogada_jogador} e o computador {jogada_computador}.', end='')
            print(f'O total deu {soma} e foi ímpar.')
            print(f'Você obteu {vitoria} ', end='')
            print('vitória.' if vitoria == 1 else 'vitórias.')
            print('-' * 40)
        break
