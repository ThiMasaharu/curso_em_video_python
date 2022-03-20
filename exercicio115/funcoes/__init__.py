def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (TypeError, ValueError):
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuário prefiriu não digitar nada.\033[m')
            return 3
        else:
            return n

def linha(tam = 40):
    return('-'*tam)

def cabecalho(texto):
    print(linha())
    print(texto.center(len(linha())))
    print(linha())

def exibir_menu(lista):
        cabecalho('MENU PRINCIPAL')
        for keys, values in enumerate(lista):
            print(f'\033[1;33m{keys+1}\033[m - \033[1;34m{values}.\033[m')
        print(linha())
        opcao = leia_int(f'\033[33mSua opção: \033[m')
        return opcao
