def ficha(nome, gols):
    print('-' * 50)
    return f'{nome} marcou {gols} gol(s) no campeonato.'

nome_jogador = input('Nome do jogador: ').strip().capitalize()
if nome_jogador == '':
    nome_jogador = '<desconhecido>'
total_gols =  input('Total de gols: ')
if total_gols.isnumeric():
    total_gols = int(total_gols)
else:
    total_gols = 0
print(ficha(nome_jogador, total_gols))
