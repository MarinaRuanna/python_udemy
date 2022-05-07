"""
MÓDULO COLLECTION: ORDERED DICT

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor = {valor}.')

OderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos.

# Fazendo import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict:

# Dicionários comuns:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  #True or False? True -> Ja que a ordem dos elementos não importa para o dicionário

# Ordered Dict:

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) #True or False? False -> no Ordered Dict a ordem dos elementos importa.

