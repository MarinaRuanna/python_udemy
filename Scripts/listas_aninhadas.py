"""
LISTAS ANINHADAS (Nested Lists)

- Algumas linguagens de programação (C/Java possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Array/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 'b', 3,234, True, 5]
"""

# EXEMPLO 1:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados:
print(listas[0])     # linha 0 - [1, 2, 3]
print(listas[0][1])  # linha 0  coluna 1 - numero 2
print(listas[2][1])  # linha 2  coluna 1 - numero 8
print(listas[2][-2]) # linha 2  coluna -2 - numero 8

# Iterando com loops uma lista aninhada:
for lista in listas:
    print(lista)

for lista in listas:
    for num in lista:
        print(num)


# List Comprehension
[[print(num) for num in lista] for lista in listas]

# OUTROS EXEMPLOS - Gerando um tabuleiro/matriz 3x3:
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha:
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais:
print([['*' for i in range(1, 4)] for j in range(1, 4)])