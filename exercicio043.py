peso = float(input('Digite seu peso em km: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
