primeiroTermo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA: '))
decimoTermo = primeiroTermo + (10-1) * razao

for i in range(primeiroTermo, decimoTermo + razao, razao):
    print('{}'.format(i), end='->')
print('Fim')
