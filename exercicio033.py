primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print ('O maior valor é o {} e o menor valor é o {}'.format(maior, menor))