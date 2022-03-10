valores = []
maior = menor = 0

for i in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        elif valores[i] < menor:
            menor = valores[i]

print('-=' * 20)
print(f'Você digitou os valores: {valores}')

print(f'Menor valor: {menor}. Posição: ', end='')
for c, i in enumerate(valores):
    if i == menor:
        print(f'{c}...', end='')
print('')

print(f'Maior valor: {maior}. Posição: ', end='')
for c, i in enumerate(valores):
    if i == maior:
        print(f'{c}...', end='')
print('')
