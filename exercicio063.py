i = 3
primeiro_termo = 0
segundo_termo = 1
proximo_termo = 0
termo = int(input('Quantos termos deseja mostrar? '))

print(f'{primeiro_termo} -> {segundo_termo} -> ', end='')

while i <= termo:
    proximo_termo = primeiro_termo + segundo_termo
    print(f'{proximo_termo} -> ', end='')
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo
    i+=1

print('Fim.')