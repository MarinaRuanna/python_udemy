"""
LEN, ABS, SUM, ROUND

len() -> Retorna o tamanho, ou seja, o número de itens de um iterável.

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.

round() -> Retona um número arrendondado para n digito de precisão após a casa decimal. Se a precisão não for informada,
retorna o inteiro mais próximo da entrada.
"""

"""
LEN

len() -> Retorna o tamanho, ou seja, o número de itens de um iterável.
"""
# REVISANDO:

# String:
print(len('Geek University'))

# Lista:
print(len([1, 2, 3, 4, 5]))

# Tupla:
print(len((1, 2, 3, 4, 5)))

# Conjunto (set):
print(len({1, 2, 3, 4, 5}))

# Dicionário:
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))


# Por debaixo dos panos, quando usamos a função len(), o Python faz o seguinte:

# Dunder Len:
print('Geek University'.__len__())

"""
ABS

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
"""

# EXEMPLOS - abs():

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

"""
SUM

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, 
incluindo o valor inicial.

# OBS: O valor inicial defalt = 0
"""

# EXEMPLOS - sum():

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -5))

# Lista:
print(sum([3.145, 5.678]))

# Tupla:
print(sum((1, 2, 3, 4, 5)))

# Conjunto (set):
print(sum({1, 2, 3, 4, 5}))

# Dicionário - Precisa informar que os valores que precisam ser somados atraves do .values():
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

"""
ROUND

round() -> Retona um número arrendondado para n digito de precisão após a casa decimal. Se a precisão não for informada, 
retorna o inteiro mais próximo da entrada.
"""

# EXEMPLOS - round():
print(round(10.2))             # 10

print(round(10.5))             # 10

print(round(10.6))             # 11

print(round(1.2121212121, 2))  # 1.21

print(round(1.219999999, 2))   # 1.22