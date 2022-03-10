salario = float(input('Digite o salário: '))

if salario > 1250:
    novoSalario = salario + (salario * 0.10)
    print('Seu salário atual R${:.2f} será aumentado para R${:.2f}'.format(salario, novoSalario))
else:
    novoSalario = salario + (salario * 0.15)
    print('Seu salário atual R${:.2f} será aumentado para R${:.2f}'.format(salario, novoSalario))
