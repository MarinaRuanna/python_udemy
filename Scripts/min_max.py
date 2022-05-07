"""
MIN E MAX

min() -> Retona o menor valor em um iterável, ou o menor de dois ou mais elementos.
Sintaxe: min (iterável, padrão = obj, chave = func)

max() -> Retorna o maior valor em um iterável, ou o maior de dois ou mais elementos.
Sintaxe: max (iterável, padrão = obj, chave = func)
"""

"""
MAX

max() -> Retorna o maior valor em um iterável, ou o maior de dois ou mais elementos.
"""

# EXEMPLO 1:
lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) # 129

set = {1, 8, 4, 99, 34, 129}
print(max(set))  # 129

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dict))  # Passa o maior valor pela chave.
print(max(dict.values()))  # 129

'''
Todos retornarão o valor 129, que é o maior nos iteráveis.
'''

# EXEMPLO 2 - Comparando dois valores:
'''
Faça um programa que receba dois valores do usuario e mostre o maior:
'''
#val1 = int(input('Informe o primeiro valor: '))
#val2 = int(input('Informe o segundo valor: '))

#print(f' o maior valor é {max(val1, val2)}')

# EXEMPLO 3 - Passando 3 valores:
print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.7891))

print(max('Geek University'))

"""
MIN

min() -> Retona o menor valor em um iterável, ou o menor de dois ou mais elementos.
"""
# EXEMPLO 1:
lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) # 1

set = {1, 8, 4, 99, 34, 129}
print(min(set))  # 1

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dict))  # Passa o menor valor pela chave.
print(min(dict.values()))  # 1

'''
Todos retornarão o valor 1, que é o menor nos iteráveis.
'''

# EXEMPLO 2 - Comparando dois valores:
'''
Faça um programa que receba dois valores do usuario e mostre o menor:
'''
#val1 = int(input('Informe o primeiro valor: '))
#val2 = int(input('Informe o segundo valor: '))

#print(f' o menor valor é {min(val1, val2)}')

# EXEMPLO 3 - Passando 3 valores:
print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.7891))

print(min('Geek University')) # O menor valor é o espaço da string.

# EXEMPLOS MAIS COMPLEXOS:

# EXEMPLO 1:
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# Levando em consideração a ordem alfabética:
print(max(nomes)) # Tim
print(min(nomes)) # Arya

# Levando em consideração o tamanho do nome:
print(max(nomes, key=lambda nome: len(nome))) # Ollivander

print(min(nomes, key=lambda nome: len(nome))) # Tim

# EXEMPLO 2:
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll', 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['titulo']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO 1:
'''
Imprima apenas o titulo da musica que mais tocou e a que menos tocou
'''

mais_toc = max(musicas, key=lambda musica: musica['tocou'])
print(mais_toc['titulo'])

menos_toc = min(musicas, key=lambda musica: musica['tocou'])
print(menos_toc['titulo'])

# Refatorando:

print(max(musicas, key=lambda musica: musica['titulo'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO 2:
'''
Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda.
'''

mais_toc = musicas[0]
for musica in musicas:
    if musica['tocou'] > mais_toc['tocou']:
        mais_toc = musica
print(mais_toc['titulo'])

menos_toc = musicas[0]
for musica in musicas:
    if musica['tocou'] < menos_toc['tocou']:
        menos_toc = musica
print(menos_toc['titulo'])

'''
Copiei um dos elementos da lista musicas e comparei as vezes que a musica tocou com todos os elementos contidos na lista,
tranformei esse elemento no maior/menor da lista e o imprimi.
'''



