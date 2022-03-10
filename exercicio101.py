def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: não vota.'
    elif 18 > idade >= 16 or idade > 70:
        return f'Com {idade} anos: voto facultativo.'
    else:
        return f'Com {idade} anos: voto obrigatório'

print(voto(int(input('Ano de nascimento: '))))