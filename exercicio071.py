valor_para_sacar = int(input('Digite o valor a ser sacado: '))
cedula = 50
total_cedula = 0
dinheiro_caixa = valor_para_sacar

while True:
    if dinheiro_caixa >= cedula:
        dinheiro_caixa -= cedula
        total_cedula += 1
    else:
        print(f'Total de {total_cedula} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if dinheiro_caixa == 0:
            break
