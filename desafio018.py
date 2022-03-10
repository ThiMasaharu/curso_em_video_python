import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo {} tem o seno de: {:.2f}'.format(angulo, seno))
print('O angulo {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo {} tem a tangente de {:.2f}'.format(angulo, tangente))