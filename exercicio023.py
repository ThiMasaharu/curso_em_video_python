numeroInformado = int(input('Digite um número: '))

#numeroString = str(numeroInformado)

#print('O número possui {} unidades'.format(numeroString[3]))
#print('O número possui {} dezenas'.format(numeroString[2]))
#print('O número possui {} centenas'.format(numeroString[1]))
#print('O número possui {} milhares'.format(numeroString[0]))

unidade = numeroInformado // 1 % 10
dezena = numeroInformado //10 % 10
centena = numeroInformado // 100 % 10
milhar = numeroInformado // 1000 % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))