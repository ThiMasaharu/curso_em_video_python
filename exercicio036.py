valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário? '))
anosParaPagar = int(input('Em quantos anos vai pagar? '))
prestacaoMensal = valorCasa / (anosParaPagar * 12)

print('\nO valor da casa é igual a R${:.2f} e será pago em {} anos'.format(valorCasa, anosParaPagar))
print('O valor da prestação a ser pago será R${:.2f}\n'.format(prestacaoMensal))

if prestacaoMensal <= 0.30 * salario:
    print('Empréstimo concedido. A prestação mensal não excede', end=' ')
    print('30% do salário informado: R${:.2f}.'.format(salario))
else:
    print('Empréstimo negado. A prestação excede', end=' ')
    print('30% do salário informado: R${:.2f}'.format(salario))