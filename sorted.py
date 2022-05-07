"""
SORTED

OBS: Não confunda, apesar do nome, com a função sort() que ja estudamos em Listas.
O sort() só funciona em Listas.

# Diferença entre sort() e sorted() em uma lista:

sort() -> Altera a lista, gerando uma lista ordenada
sorted() -> Cria uma nova lista. Não altera a lista original.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar elementos.

O sorted() SEMPRE retorna uma lista com os elementos do iterável ordenados.
"""

# EXEMPLO 1 - lista:
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordena do menor para o maior.

print(numeros)         # NÃO altera a lista

# EXEMPLO 2 - Tupla:
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros)) # Retorna uma lista ordenando do menor para o maior.

print(numeros)         # NÃO altera a tupla

# EXEMPLO 3 - Set:
numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Retorna uma lista ordenando do menor para o maior.

print(numeros)         # NÃO altera o conjunto

# Adicionando parâmetros ao sorted():
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos converter para outros tipos de iteravel:

# Tupla:
print(tuple(sorted(numeros, reverse=True))) # Ordena do maior para o menor

# Set:
print(set(sorted(numeros, reverse=True))) # Ordena do maior para o menor

# EXEMPLO - Mais complexos:

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], 'cor': 'amarelo'},
    {"username": "doggo", "tweets": ["Eu adoro cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], 'cor': 'preto', 'musica': 'rock'},
]

print(usuarios)

# Ordenando pelo tamanho do dicionário:
print(sorted(usuarios, key=len))  # Crescente - Ordena pelo tamanho dos dicionários, do menor para o maior.
print(sorted(usuarios, key=len, reverse=True))  # Decrescente - Ordena pelo tamanho dos dicionários, do maior para o menor.

# Outras maneiras:
print(sorted(usuarios, key=lambda usuario: len(usuario)))  # Crescente - Ordena pelo tamanho dos dicionários, do menor para o maior.

# Ordenando pela quantidade de tweets:
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


# Ordenando pela ordem alfabetica dos username:
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# EXEMPLO - Ordenando lista de musica:

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll', 'tocou': 32},

]

# Ordena da menos tocada para a mais tocada:
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada:
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

# Ordenando por tamanho do titulo:
print(sorted(musicas, key=lambda musica: len(musica['titulo'])))

print(sorted(musicas, key=lambda musica: len(musica['titulo']), reverse=True)) # Do maior para o menor

# Ordenando por ordem alfabética do titulo:
print(sorted(musicas, key=lambda musica: musica['titulo']))
