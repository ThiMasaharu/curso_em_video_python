primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = float(input('Digite a razão da P.A.: '))
termo = 1
i = primeiro_termo
mais_termos = 1
total = 10

while mais_termos != 0:
    while termo <= total:
        print(f'{i} -> ', end='')
        i += razao
        termo += 1
    print('Pausa.')
    mais_termos = int(input('Quantos termos a mais você quer? '))
    total += mais_termos

print(f'P.A. finalizada com {total} termos no total.')
