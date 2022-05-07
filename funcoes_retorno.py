"""
FUNÇOES COM RETORNO
"""
numeros = [1, 2, 3]

print(numeros)

ret_pop = numeros.pop()

print(f'Retorno de pop {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print {ret_pr}')
'''
OBS: Em Python, quando uma função não retorna nenhum valor o retorno é None.

OBS: Funções Python que retornam vaores, devem retornar esses valores com a palavra reservada return.

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passar a execução
da função para outras funções ou mesmo para o print.
'''

# Exemplo de função:

def quadrado_de_sete():
    print(7 * 7)

ret = quadrado_de_sete()

print(f'Retorno de ret {ret}')

# Vamos refatorar(reescrever/redefinir/modificar para melhorar o código) essa função para que ela retorne o valor:

def quadrado_de_sete():
    return 7 * 7

# Criamos uma variavel para receber o retorno da função.
ret = quadrado_de_sete()

print(f'Retorno {ret}')

print(f'Retorno { quadrado_de_sete() + 1}')

# Refatorando a primeira função:

def diz_oi():
    return 'oi '

alguem = 'Marina!'

print(diz_oi() + alguem)

'''
OBS: Sobre a palavra reservada 'return':
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado, e até mesmo multiplos valores;
'''

# EXEMPLO 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado apos o retorno...')
    return 'oi!'
    print('Estou sendo executado apos o retorno...')

print(diz_oi())


# EXEMPLO 2 - Podemos ter, em uma função, diferentes returns;
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# EXEMPLO 3 - Podemos, em uma função, retornar qualquer tipo de dado, e até mesmo multiplos valores;
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())

print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda:

from random import random

def joga_moeda():
    # Gera um numero pseudo-randômico entre 0 e 1.
    if random() > 0.5:
        return 'cara'
    return 'Coroa'

print(joga_moeda())


# Erros comuns na utilização do retorno de uma função, que na verdade não são erros, mas codifivação desnecessarias:

def eh_impar():
    numero = 6
    if numero % 2 != 0: # % modulo, ou seja, resto da divisão pelo numero inserido em seguida, no caso do exemplo é o numero 2. Caso p resto de divisão por 2 seja diferente de zero, o numero é impar.
        return True     # Caso o resto de divisão seja 0, o numero é par.
    return False

print(eh_impar())
