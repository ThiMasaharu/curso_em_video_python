from datetime import date

anoNascimento = int(input('Digite o ano que nasceu: '))
idade = date.today().year - anoNascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Ainda vai se alistar.')
    anosEspera = 18 - idade
    print('Faltam {} ano(s)'.format(anosEspera))
else:
    print('Já passou da hora de se alistar!')
    anosAtrasados = idade - 18
    print('Você está {} ano(s) atrasados.'.format(anosAtrasados))
