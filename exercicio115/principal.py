from funcoes import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivo_existe(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criar_arquivo(arq)

lista_opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
while True:
    opcao = exibir_menu(lista_opcoes)
    if opcao == 1:
        # Opção de listar o conteúdo de um arquivo! 
        ler_arquivo(arq)
    elif opcao == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Encerrando o programa... Até mais!')
        break
    else:
        print((f'\033[31mERRO! Digite uma opção do menu.\033[m'))
    sleep(1) 
