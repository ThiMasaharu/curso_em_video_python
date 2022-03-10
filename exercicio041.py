from datetime import date

anoNascimento = int(input('Digite o ano que nasceu: '))
idade = date.today().year - anoNascimento

print('O atleta possui {} anos'.format(idade))

if idade <= 9:
    print('Atleta categoria mirim')
elif idade <= 14:
    print('Atleta categoria infantil')
elif idade <= 19:
    print('Atleta categoria junior')
elif idade <= 25:
    print('Atleta categoria sênior')
else:
    print('Atleta categoria master')
