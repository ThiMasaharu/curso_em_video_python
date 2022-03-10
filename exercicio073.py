tabela_brasileirao = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians',
'Bragantino','Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional',
'São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport Recife',
'Chapecoense')

print('-='*40)
print(f'Tabela do brasileirão: {tabela_brasileirao}')
print('-='*40)
print(f'5 primeiros colocados: {tabela_brasileirao[:5]}')
print('-='*40)
print(f'Últimos 4 colocados: {tabela_brasileirao[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('-='*40)
print(f'Chapecoense está na {tabela_brasileirao.index("Chapecoense")+1}ª posição.')
print('-='*40)
