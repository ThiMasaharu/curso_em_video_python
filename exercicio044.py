print('{:=^40}'.format(' Lojas Thiago '))

valorInicial = float(input('Digite o valor: '))

print('''Formas de pagamento:
[1] à vista com dinheiro/cheque;
[2] à vista no cartão;
[3] até duas vezes no cartão;
[4] três vezes ou mais no cartão.''')
opcao = int(input('Qual a opção desejada? '))

if opcao == 1:
    print('Pagamento em dinheiro ou cheque. O cliente terá 10% de desconto.')
    print('O valor inicial R${:.2f} passa a valer R${:.2f}'.format(valorInicial, valorInicial-(valorInicial*0.1)))
elif opcao == 2:
    print('Pagamento à vista no cartão. O cliente terá 5% de desconto.')
    print('O valor inicial R${:.2f} passa a valer R${:.2f}'.format(valorInicial, valorInicial-(valorInicial*0.05)))
elif opcao == 3:
    print('Pagamento parcelado em 2 vezes sem juros de R${:.2f}.'.format(valorInicial/2))
    print('O valor total a ser pago no final será R${:.2f}'.format(valorInicial))
elif opcao == 4:
    parcela = int(input('Digite a quantidade de parcelas: '))
    valorFinal = valorInicial + (valorInicial * 0.2)
    valorParcelado = valorFinal / parcela

    print('O valor será parcelado em {} vezes com juros de R${:.2f}.'.format(parcela, valorParcelado))
    print('O valor inicial R${:.2f} no final valerá R${:.2f}.'.format(valorInicial, valorFinal))
else:
    print('Opção inválida.')
