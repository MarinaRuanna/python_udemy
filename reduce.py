"""
REDUCE

OBS: A partir do Python versão 3+ a função reduce() não é mais uma função integrada (Built-in),
Agora temos que importar e utilizar esta função a partir do módulo 'functools'.

Guido Van Rossum: 'Utilize a função reduce() se você realmente precisa dela.
Em todo caso, 99% das vezes um loop for é mais legível.

# Para entender o reduce():
Imagine que você tem uma coleção de dados:?

dados = [a1, a2, a3, ..., an]

E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter, a função reduce() recebe dois parâmetros: A função e o iterável.
reduce(função, dados)

A função reduce() funciona da seguinte forma:
    - Passo 1: res1 = f(a1, a2)    # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    - Passo 2: res1 = f(res1, a3)  # Aplica a função passando o resultado do Passo 1 mais o terceiro elemento,
                                     e guarda o resultado.
    Isso é repetido até o final.
    - Passo 3: res3 = f(res2, a3)
    .
    .
    .
    - Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumentos o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...) an)
"""

# Função reduce() na prática:
'''
Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista:
'''
# Fazendo o import:

from functools import reduce

dados = [1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce precisamos de uma função que receba dois parâmetros.

mult = lambda x, y: x * y

res = reduce(mult, dados)
print(res)                 # Retorna a mutiplicação de todos os dados da lista.

# Utilizando um loop normal:
res = 1
for n in dados:
    res = res * n

print(res)