lista = []

for i in range (0,5):
    valor_a_adicionar = int(input('Digite um valor: '))
    
    if i == 0 or valor_a_adicionar > lista[len(lista)-1]:
        lista.append(valor_a_adicionar)
        print('Adicionado ao final da lista...')
    else:
        j = 0
        while j < len(lista):
            if valor_a_adicionar <= lista[j]:
                lista.insert(j, valor_a_adicionar)
                print(f'Adicionado na posição {j} da lista')
                break
            j += 1

print(f'Os valores digitados em ordem na lista foram: {lista}')
