expressao = str(input('Digite uma frase: ')).strip().upper()
palavras = expressao.split()
junto = ''.join(palavras)
inverso = junto[::-1]

# Não é necessário for. Dá para utilizar o que está no inverso
'''for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]'''

print(expressao, inverso)

if inverso == junto:
    print('O que você digitou é um palíndromo.')
else:
    print('Não é palíndromo.')
