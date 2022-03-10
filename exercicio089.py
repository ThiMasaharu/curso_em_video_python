lista_dados = []
lista_pessoas = []

while True:
    lista_dados.append(input('Nome: ').strip().capitalize())
    lista_dados.append(int(input('Nota 1: ')))
    lista_dados.append(int(input('Nota 2: ')))

    lista_pessoas.append(lista_dados[:])
    lista_dados.clear()
    
    resposta_continua = input('Deseja continuar [S/N]? ').strip()[0]
    while resposta_continua not in 'SsNn':
        resposta_continua = input('Inválido. Tente novamente [S/N]: ').strip()[0]
    
    if resposta_continua in 'Nn':
        print('-=' * 30)
        break

print(f'Nº. Nome               Média')
print(f'-' * 30)
for i in range(0, len(lista_pessoas)):
    print(f'{i}', f' {lista_pessoas[i][0]}', end = '') # nº e nome
    print(f' {((lista_pessoas[i][1] + lista_pessoas[i][2]) / 2):>15}') # media da nota
print(f'-' * 30)

while True:
    mostrar_aluno = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    
    if mostrar_aluno == 999:
        break
    
    if mostrar_aluno <= len(lista_pessoas)-1:
        print(f'Notas de {lista_pessoas[mostrar_aluno][0]}: {lista_pessoas[mostrar_aluno][1]}', end=' e ')
        print(f'{lista_pessoas[mostrar_aluno][2]}')
print('Programa finalizado. Volte sempre.')