"""
MAPAS ->  Conhecidos em Python como Dicionários.

Dicionários em Python sõa representados por {}
"""

receita = {'jan': 100, 'fev': 250, 'mar':400}

print(receita)

# Interar sobre dicionários:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'em {chave} revebi R$ {receita[chave]}')

# Acessando as chaves:
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores:
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionárioos:
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# Soma*, Valor Maximo*, Valor Minimo* e Tamanho:

# * Se os valores forem todos inteiros e reais

print(sum(receita.values())) # soma
print(max(receita.values())) # valor maximo
print(min(receita.values())) # Valor minimo
print(len(receita)) # tamanho










