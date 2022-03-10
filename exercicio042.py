print ('-=' * 20)
print ('Analisador de triângulos')
print ('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    if r1==r2==r3:
        print('Pode-se formar um triângulo equilátero.')
    elif r1==r2 or r2==r3 or r1==r3:
        print('Pode-se formar um triângulo isósceles.')
    else:
        print('Pode-se formar um triângulo escaleno.')
else:
    print('Não é possível formar triângulo.')
