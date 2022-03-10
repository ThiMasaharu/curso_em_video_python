quantidadeKm = float(input('Quantos quilômetros foram rodados? '))
diasAlugados = int(input('Quantos dias o carro foi alugado? '))

precoParaPagar = (quantidadeKm * 0.15) + (diasAlugados * 60)

print ('Preço a pagar: {}'.format(precoParaPagar))