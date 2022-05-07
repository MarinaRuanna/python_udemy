"""
ZIP

zip() -> Cria um iterável chamado 'Zip Object' que agrega elemento de cada um dos iteráveis
passados como entrada em pares.
"""

# EXEMPLO 1:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla, Conjunto (set) ou Dicionário:
'''
OBS: Assim como no map() e filter() os dados são esvaziados após a primeira execução.
'''

# Lista:
print(list(zip1))

# Tupla:
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

# Conjunto (set):
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

# Dicionário - Precisa informar que os valores que precisam ser somados atraves do .values():
zip1 = zip(lista1, lista2)
print(dict(zip1))

# EXEMPLO 2:
'''
O zip() utiliza como parâmetro o menor tamanho em iterável. isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.
'''
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com o zip():

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# lista de tuplas:
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# EXEMPLOS MAIS COMPLEXOS:

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map():

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))