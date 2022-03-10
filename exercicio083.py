parenteses_abrindo = []
parenteses_fechando = []
pilha = []
expressao = str(input('Digite a expressão: '))

'''for i, j in enumerate(expressao):
    if '(' in j:
        parenteses_abrindo.append('(')
    elif ')' in j:
        parenteses_fechando.append(')')
    i+=1

if len(parenteses_abrindo) == len(parenteses_fechando):
    print('Expressão válida.')
else:
    print('Expressão inválida.')'''

# Solução Guanabara (a minha funciona ainda.)
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')