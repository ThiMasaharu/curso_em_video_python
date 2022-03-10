nomeInteiro = str(input('Digite seu nome inteiro: ')).strip()
nomeDivido = nomeInteiro.split()

print('Seu primeiro nome é: {}'.format(nomeDivido[0]))
print('Seu último nome é: {}'.format(nomeDivido[len(nomeDivido) - 1]))