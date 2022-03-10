nome = input('Digite nome completo: ').strip()

print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Quantas letras seu nome possui: {}'.format(len(nome) - nome.count(' ')))
nomeSeparado = nome.split()
print('Seu primeiro nome possui {} letras'.format(len(nomeSeparado[0])))