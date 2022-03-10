print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print('É possível formar um triângulo')
else:
    print ('Não pode formar um triângulo')