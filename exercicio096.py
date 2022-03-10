def calcula_area(largura, comprimento):
    print(' Controle de terrenos ')
    print('-' * 30)
    area = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {area}m².')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
calcula_area(l, c)