valor = input('Digite algo: ')

print('O tipo primitivo é ', type(valor))
print('Valor é numérico?', valor.isnumeric())
print('Valor é alfanumérico?', valor.isalnum())
print('Valor é alfabético?', valor.isalpha())
print('O valor é apenas espaço?', valor.isspace())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está em maiúsculas e minúsculas? (capitalizado)', valor.istitle())