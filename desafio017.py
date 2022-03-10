from math import hypot

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = (hypot(catetoOposto, catetoAdjacente))

print ('O cateto oposto {} e adjacente {}'.format(catetoOposto, catetoAdjacente),end=' ')
print ('tem como hipotenusa {:.2f}'.format(hipotenusa))