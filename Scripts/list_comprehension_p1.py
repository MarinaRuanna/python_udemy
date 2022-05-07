"""
LIST COMPREHENSION - Parte 1

- utilizando List Comprehension, nós podemos podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension:

[ dado for dado in iterável ]
"""

# EXEMPLOS
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

'''
Para entender melhor o que está acontecendo devemos dividir a expressão em duas parte, sendo elas:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
'''

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [ funcao(numero) for numero in numeros]
print(res)

# List Comprehension VS Loop:

# Loop:
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# Loop - Refatorado:
for numero in numeros:
    numeros_dobrados.append(numero * 2)


# List Comprehension:
print([numero * 2 for numero in numeros])

# OUTROS EXEMPLOS:

#EXEMPLO 1:
nome = 'Geek University'

print([letra.upper() for letra in nome])

# EXEMPLO 2:
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo[0].upper() for amigo in amigos]) # Apresenta apenas a primeira letra maiuscula em uma lista.

def caixa_alta(nome):
    nome =  nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# Refatorando:

print([amigo.title() for amigo in amigos])

# EXEMPLO 3:
print([numero * 3 for numero in range(1, 10)])

# EXEMPLO 4:
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# EXEMPLO 5:
print([str(numero) for numero in [1, 2, 3, 4, 5]])