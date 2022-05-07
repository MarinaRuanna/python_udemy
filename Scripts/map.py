"""
MAP

Com map, fazemos mapeamento de valores para uma função.
"""

import math

def area(r):
    """Calcula a area de um círculo com o 'r'"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum:
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map:
'''
Map é uma função que recebe dois parâmetros: O primeiro uma função e o segundo, um iterável. Retorna um 'map object'
'''
areas = map(area, raios) # Pega os dados iteraveis da lista e passa como entrada para a função.

print(areas)  # Retorna um 'map object'

print(type(areas))

print(list(areas)) # Convertendo em uma lista, tambem pode ser convertido em tupla, dicionário e set (conjunto).

print(list(areas))  #  Após utilizar a função map(), depois da primeira utilização do resultado, ele zera.


# Forma 3 - Map com Lambda:
'''
OBS 1: No map, geralmente se usa uma expressão lambda e não uma função definida anteriormente.
'''
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Para fixar - Map:
'''
Temos dados iteráveis:
- dados: a1, a2, ..., an

Temos uma função:
- Função: f(x)

Utilizamos a função: map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função. 

O Map Object gerado: f(a1), f(a2), ..., f(an) 
'''

# EXEMPLO:
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

# Convertendo a temperatura das cidades de Celsios para Fahrenheit usando lambda:
'''
A formula de conversão de graus Celsius para Fahrenheit é :
f = 9/5 * c + 32
'''

c_para_f = lambda dado:(dado[0], round((9/5) * dado[1] + 32)) # round() irá transformar o resultado em um numero inteiro.
print(list(map(c_para_f, cidades)))



