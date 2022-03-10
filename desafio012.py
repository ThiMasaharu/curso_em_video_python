n1 = float(input('Digite o preço: '))
porcentagem = 0.05*n1
desconto = n1-porcentagem

print('Desconto de R${:.2f}\nO valor será R${:.2f}'.format(porcentagem, desconto))