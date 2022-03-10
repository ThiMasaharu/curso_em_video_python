jogador = {}
total_gol = []

jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for i in range(0, partidas):
    total_gol.append(int(input(f'Quantos gols na partida {i+1}: ')))
jogador['gols'] = total_gol
jogador['total'] = sum(total_gol, 0)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor {values}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'Na partida {i+1}, {jogador["nome"]} marcou {jogador["gols"][i]}.')
print(f'Foi um total de {jogador["total"]} gols.')
