from datetime import datetime

dicionario = {}
dicionario['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = datetime.now().year - nascimento
dicionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: '))
    dicionario['aposentadoria'] = (dicionario['contratação'] + 65) - (datetime.now().year)

print('-='*30)
for keys, values in dicionario.items():
    print(f'- {keys}: {values}.')
