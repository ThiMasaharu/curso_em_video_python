n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('Sua média foi {:.1f} e infelizmente está reprovado.'.format(media))
elif 7 > media >= 5:
    print('Sua média foi {:.1f} e está de recuperação.'.format(media))
elif media > 7:
    print('Parabéns! Sua média foi {:.1f} e você foi aprovado!'.format(media))
