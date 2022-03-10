nome_e_produto = ('Lápis', 1.75,
                'Borracha', 2,
                'Caderno', 15.90,
                'Estojo', 25,
                'Transferidor', 4.20,
                'Compasso', 9.99,
                'Mochila', 120.32,
                'Canetas', 22.30,
                'Livro', 34.90)

print('-=' * 20)
print(f'{"Lista de preços":^40}')
for i in range (0, len(nome_e_produto)):
    if i % 2 == 0:
        print(f'{nome_e_produto[i]:-<30} ', end='')
    else:
        print(f'R${nome_e_produto[i]:>8.2f}')
print('-=' * 20)