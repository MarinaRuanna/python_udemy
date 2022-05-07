"""
SET COMPREHENSION

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5} # Não aceita valores repetidos, não guarda ordenação.
"""

# EXEMPLO 1:
numeros = {num for num in range(1, 7)}
print(numeros)

# EXEMPLO 2:
numeros = {x ** 2 for x in range(10)}
print(numeros)

'''
DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set.
'''

numeros = {x: x ** 2 for x in range(10)} # Adição de uma chave transforma o set in dict.
print(numeros)

# EXEMPLO 3:
letras = {letra for letra in 'Geek University'}
print(letras)             # Gera um conjunto (set) sem repetição de elementos e sem ordenação.

