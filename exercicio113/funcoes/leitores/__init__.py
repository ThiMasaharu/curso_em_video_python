def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário prefiriu não informar valor.\033[m')
            return 0
        else:
            return n  
    
def leia_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (TypeError, ValueError):
            print(f'\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário prefiriu não informar os valores.\033[m')
            return 0
        else:
            return n