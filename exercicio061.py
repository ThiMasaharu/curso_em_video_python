primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = float(input('Digite a razão da P.A.: '))
termo = 1
i = primeiro_termo

while termo <= 10:
    print(f'{i}', end='')
    print(' -> ' if termo < 10 else ' -> Fim.', end='')
    i += razao
    termo +=1
