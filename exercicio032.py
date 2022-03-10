from datetime import date

ano = int(input('Qual é o ano? Digite 0 caso queira o ano atual: '))

if ano == 0:
    ano = date.toyday().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
