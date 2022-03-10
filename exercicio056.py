somaIdade = 0
idadeHomem = 0
homemMaisVelho = ''
MulheresComMenosDeVinte = 0

for pessoa in range (1, 5):
    print('{}ª pessoa.'.format(pessoa))
    
    nome = str(input('Digite o nome: ')).capitalize().strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaIdade += idade

    if sexo == 'M' and idade > idadeHomem:
        idadeHomem = idade
        homemMaisVelho = nome

    if sexo == 'F' and idade < 20:
        MulheresComMenosDeVinte += 1

mediaIdade = somaIdade / 4

print('A média de idade do grupo é igual a {:.2f}.'.format(mediaIdade))
print('O homem mais velho do grupo se chama {}.'.format(homemMaisVelho))
print('Existem {} mulheres com menos de 20 anos.'.format(MulheresComMenosDeVinte))
