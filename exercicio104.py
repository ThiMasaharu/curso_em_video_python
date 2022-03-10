def leia_int(mensagem):
    n = input(mensagem)
    while n.isnumeric() == False:
        n = input('ERRO! Digite um número inteiro válido: ')
    return f'Você acabou de digitar o número {n}.'

print(leia_int('Digite um número: '))