zero_a_vinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito'
'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')

valor = int(input('Digite um número de 0 a 20: '))

while valor not in range (0, 21):
    valor = int(input('Número inválido. Digite um número de 0 a 20: '))

print(zero_a_vinte[valor-1])