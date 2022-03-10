from random import randint

aleatorio = randint(0, 5)
chuteUsuario = int(input('Qual número eu pensei? '))

if chuteUsuario == aleatorio:
    print('Você acertou! O número era {}'.format(aleatorio))
else:
    print ('Tente novamente. O número era {}'.format(aleatorio))
