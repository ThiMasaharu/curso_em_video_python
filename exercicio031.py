from time import sleep


distancia = float(input('Qual a distância viajada em Km? '))

print ('Você está prestes a viajar {}Km'.format(distancia))
print ('Calculando preço...')
sleep(2)

if distancia <= 200:
    precoPassagem = distancia * 0.50
else:
    precoPassagem = distancia * 0.45

print('O valor da passagem custará R${:.2f}'.format(precoPassagem))