"""
REVERSED

OBS: Não confunda com a função reverse() que estudamos em Listas, que inverte a ordem da lista.

reverse() -> Funciona apenas nas Listas

reversed() - Funciona com qualquer iterável. Sua função é inverter o iteravel.
"""

# EXEMPLO - Tipo de objeto que o reversed() retorna:
'''
A função reversed() retorna um iterável chamado List Reversed Iterator
'''
lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)        # Retorna list_reverseiterator object

print(type(res))  # list_reverseiterator

# Podemos converter o elemento retornado para uma Lista, Tupla ou conjunto (set):

# Lista:
print(list(reversed(lista)))

# Tupla:
print(tuple(reversed(lista)))

# Conjunto (set):
print(set(reversed(lista)))  # Em conjunto (set) não definimos a ordem dos elementos.

# Podemos iterar sobre o reversed():
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for:
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de string:
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso:
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range():
for n in range(9, -1, -1):
    print(n)


