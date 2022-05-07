"""
TIPO BOOLEANO
Albegra Booleana, criada por George Boole

2 constantes, verdadeiro ou falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscúla

ERRADO:
true, false

CERTO:
True, False
"""
ativo = True
print(ativo)

"""
OPERAÇÕES BÁSICAS
"""

# negação (not):
"""
Fazendo a negação, se o valor booleanofor verdadeiro o resultado será falso, se for falso, o resultado será verdadeiro, ou seja, sempre o contrario.
"""
print(not ativo)

logado = False

# ou (or):
""" 
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True - > True
True or False -> True 
False or True -> True 
False or False -> False
"""

print(ativo or logado)

# e (and):
"""
Também é uma operação binárioa, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
print(ativo and logado)



