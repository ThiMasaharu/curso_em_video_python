from exercicio107 import moeda

preco = float(input('Digite o preco: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}.')
print(f'O dobro de R${preco} é {moeda.dobro(preco)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}.')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10)}.')
