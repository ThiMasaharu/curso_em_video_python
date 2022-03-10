dado_pessoa = {}
pessoas = []
soma_idade = 0

while True:
    dado_pessoa['nome'] = input('Nome: ').strip().capitalize()
    dado_pessoa['sexo'] = input('Sexo [M/F]: ').strip()[0]
    
    while dado_pessoa['sexo'] not in 'MmFf':
        dado_pessoa['sexo'] = input('Sexo inválido. Digite M ou F: ').strip()[0]

    dado_pessoa['idade'] = int(input('Idade: '))
    pessoas.append(dado_pessoa.copy())
    soma_idade += dado_pessoa['idade']

    resposta_continuar = input('Deseja continuar [S/N]? ').strip()[0]
    while resposta_continuar not in 'SsNn':
        resposta_continuar = input('Inválido. Digite S ou N: ').strip()[0]
    if resposta_continuar in 'Nn':
        media = soma_idade / len(pessoas)
        break

print(dado_pessoa)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')

for individuo in pessoas:
    if individuo['sexo'] in 'Ff':
        print(f'C) As mulheres cadastradas foram {individuo["nome"]}', end=' ')
print('.')

print(f'D) Lista de pessoas com a idade acima da média:')
for individuo in pessoas:
    if individuo['idade'] > media:
        print(f'Nome: {individuo["nome"]}; Sexo: {individuo["sexo"]}; Idade: {individuo["idade"]}')
print('<< Encerrado >>')
