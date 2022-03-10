def escreva(texto):
    tamanho_texto = len(texto) + 4
    print('~' * tamanho_texto)
    print(texto)
    print('~' * tamanho_texto)

entrada_usuario = input('Digite algo: ')
escreva(entrada_usuario)