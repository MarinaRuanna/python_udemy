"""
HIGHER ORDER FUNCTIONS - HOF - Funções de Maior Grandeza

O que isso significa?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam funções como resultado ou
mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções nos
nossos programas.

OBS: Na seção de funções, nos utilizamos isso.

Em Python as funções são cidadões de primeira classe (Frist Class Citizen).
"""

# EXEMPLO - Definindo as funções:

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções:

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas:
'''
Em Python, podemos tambem ter funções dentro de funções, que são conhecidas por Nested Functions ou também 
Inner Functions (Funções Internas)
'''

# EXEMPLO:

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Eai!', 'Suma daqui!', 'Gosto muito de você!'))
    return humor() + pessoa

# Testando:

print(cumprimento('Marina'))

print(cumprimento('Ruanna'))

# Retornando funções de outras funções:

def faz_me_rir():
    def rir():
        return choice(('kkkkkkkkk', 'hahahaha', 'rsrsrsrsrsr'))
    return rir

# Testando:

rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funções Internas/ Nested Functions) podem acessar o escopo de funções mais externas:

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('heheheheheh', 'lololololololo', ' hihihihihihihi'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando:

riso = faz_me_rir_novamente('Marina')

print(riso())
print(riso())
print(riso())


