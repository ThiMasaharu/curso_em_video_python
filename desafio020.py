import random

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro,segundo,terceiro,quarto]

random.shuffle(lista)

print ('A ordem de apresentação sorteado foi {}'.format(lista))