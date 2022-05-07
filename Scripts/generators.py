"""
GENERATOR EXEPRESSION

Em aulas anteriores, estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension.

Não vimos:
- Tuple Comprehension ...Porque elas se chamam Generators.

# EXEMPLO - Aulas anteriores com List Comprehension:
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
"""

# EXEMPLO - Com Generators:
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes)) # Não é um List Comprehension

'''
- Gera um Generator Object. Depois de executado os dados são apagados.
'''

# List Comprehension:
res = [nome[0] == 'C' for nome in nomes]
print(type(res))     # Class List
print(res)

# Generator:
res = (nome[0] == 'C' for nome in nomes)
print(type(res))     # Class Generator - Gasta menos recurso da memória.
print(res)


# ENTENDENDO PERFORMANCE:

# Qual a utilidade de getsizeof? -> Retona a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória:
print(getsizeof('Geek'))  # 53 bytes

# Quanto maior a string, mais espaço ocupa:
print(getsizeof('University')) # 59 bytes

print(getsizeof(9)) # 28 bytes

print(getsizeof(91)) # 28 bytes

print(getsizeof(92345668823)) # 32 bytes

print(getsizeof(True)) # 28 bytes

# COMPARANDO PERFORMANCE:

# Gerando uma lista de números com uma List Comprehension:
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com uma Set Comprehension:
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com uma Dictionary Comprehension:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com uma Generator:
gen = getsizeof(x * 10 for x in range(1000))

print(f'Para fazer a mesma tarefa, gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator: {gen} bytes')

# Iterando no Generator Expression:
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

