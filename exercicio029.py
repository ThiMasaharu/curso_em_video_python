velocidade = int(input('Qual é a velocidade? '))


if velocidade > 80:
    valorMulta = (velocidade-80) * 7
    print('Você excedeu o limite de velocidade!', end=(' '))
    print('Você vai pagar R${:.2f}'.format(valorMulta))
else:
    print('Tenha um bom dia!')