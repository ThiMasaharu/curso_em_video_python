cidade = input('Digite a cidade: ').strip()

# verifica se começa com santo (foi usado upper para evitar as variações)
print(cidade[:5].upper() == 'SANTO')