frase = str(input('Digite uma frase: ')).strip().lower()

print(frase.count('a'))
print('A letra "a" aparece primeiro na posição {}'.format(frase.find('a') + 1))
print('A letra "a" aparece por último na posição {}'.format(frase.rfind('a') + 1))
