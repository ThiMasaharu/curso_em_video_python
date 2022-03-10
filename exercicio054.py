from datetime import date

menor = 0
maior = 0

for i in range(0, 7):
    anoNascimento = int(input('Digite o ano que nasceu: '))
    comparacaoIdade = date.today().year - anoNascimento
    if comparacaoIdade <= 18:
        menor += 1
    else:
        maior += 1

print('Existem {} maiores de idade e {} menores de idade'.format(maior, menor))
