pessoas = {}
pessoas['nome'] = input('Nome: ').strip().capitalize()
pessoas['média'] = float(input(f'Média de {pessoas["nome"]}: '))

if pessoas['média'] >= 7:
    pessoas['situação'] = 'Aprovado'
elif 7 > pessoas['média'] >= 5:
    pessoas['situação'] = 'Recuperação'
else:
    pessoas['situação'] = 'Reprovado'

print('-=' * 30)
for i, j in pessoas.items():
    print(f'{i}: {j}')
