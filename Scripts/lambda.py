"""
LAMBDAS

conhecidas por Expressões Lambdas, ou simplismente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Funções em Python:
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda:
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

"""

# Podemos ter expressões lambdas com mútiplas entradas:
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('marina', 'ruanna'))
print(nome_completo('    MARINA', 'ruanna'))
print(nome_completo(' marina  ', '  rUANNa        '))

# Em Python podemos ter nenhuma ou várias entradas. Em lambda também.

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y +1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados, teremos erro TypeError.

# EXEMPLO 1:

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frenk Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett' ]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Função Quadrática:
# f(x) = a * x ** 2 + b * x + c

# Definindo a função:
def geradora_funcao_quadratica(a, b, c):
    '''Retorna a função f(x) = a * x ** 2 + b * x + c'''
    return lambda x: a * x ** 2 + b * x + c

print(geradora_funcao_quadratica(2, 3, -5))

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))


# Usando .join():

my_list = ['Geek', 'University']


def juntar_str(x):
    return ''.join(x)

print(juntar_str(my_list))



# Usando .join() em lambda:

f = (lambda x: ''.join(x))

print(f(my_list))

