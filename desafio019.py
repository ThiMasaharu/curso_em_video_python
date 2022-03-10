import random

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')
listaAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

print('O aluno sorteado foi {}'.format(random.choice(listaAlunos)))