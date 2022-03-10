integer = int(input('Digite um número inteiro: '))
print('''Digite 1 para converter para binário
2 para octal
3 para hexadecimal''')
escolhaUsuario = int(input('Qual a sua opção? '))

if escolhaUsuario == 1:
    print('Valor binário correspondente: {}'.format(bin(integer)))
elif escolhaUsuario == 2:
    print('Valor octal correspondente: {}'.format(oct(integer)))
elif escolhaUsuario == 3:
    print('Valor hexadecimal correspondente: {}'.format(hex(integer)))
else:
    print('Opção inválida! Tente outra opção.')
    