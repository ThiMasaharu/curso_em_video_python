from time import sleep


jogador = {}
total_gol = []
jogadores = []

while True:
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    for i in range(0, partidas):
        total_gol.append(int(input(f'Quantos gols na partida {i+1}: ')))
    jogador['gols'] = total_gol[:]
    jogador['total'] = sum(total_gol, 0)
    jogadores.append(jogador.copy())
    total_gol.clear()

    resposta_continuar = input('Deseja continuar [S/N]? ').strip()[0]
    while resposta_continuar not in 'SsNn':
        resposta_continuar = input('Inválido. Digite S ou N: ').strip()[0]

    if resposta_continuar in 'Nn':
        break
    
print('-=' * 40)
print(f'cod {"nome":<15} gols {"total":<10}')
print('-' * 80)
for keys, values in enumerate(jogadores):
    print(f'{keys:>3} {values["nome"]:<15} {values["gols"]} {values["total"]:<10}')

while True:
    codigo = int(input('Mostrar dados de qual jogador [999 para parar]? '))
    if codigo == 999:
        print('<< Encerrado >>')
        break

    if codigo < len(jogadores):
        print(f'Levantamento do jogador {jogadores[codigo]["nome"]}:')
        for keys, values in enumerate(jogadores[codigo]['gols']):
            print(f'{jogadores[codigo]["nome"]} marcou {values} no jogo {keys+1}')
            sleep(1)
    else:
        print(f'Jogador {codigo} não existe.')
