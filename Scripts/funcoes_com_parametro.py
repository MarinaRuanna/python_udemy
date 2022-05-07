"""
FUNÇÕES COM PARAMETRO (de entrada)

-  Funções que recebem dados para serem processados dentro da mesma.

Se a gente pensar em um programa qualquer, geralmente temos:
    Entrada -> Processamento -> Saída

Se a gente pensar em função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mais possuem saída;
- Não possuem entrada nem saída.
"""

# Refatorando uma função:


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando a função:


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Patricia')

'''
Funções podem ter 'n' parametros de entrada, ou seja, podemos receber como entrada em uma função, quantos parametros
forem necessarios. Eles são separados por virgula (,).
'''

# EXEMPLO 1:


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) *msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um numero errado de paramentros ou argumentos, teremos o erro TypeError.
'''
print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais.
print(soma(4)) # TypeError - Passando argumentos a menos.
'''

# Nomeando parâmetros:


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}.'


print(nome_completo('Marina', 'Ruanna'))

'''
# Diferenças entre Parâmetros e Argumentos:

- Parâmetros são variáveis declaradas na definição de uma função;
- Argumentos são dados passados durante a execução de u,a função.
'''

# A ordem dos parâmetros importa:

nome = 'Marina'
sobrenome = 'Ruanna'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments):
'''
Caso utilizemos nomes dos parâmetros para informa-los, podemos utilizar qualquer ordem.
'''

print(nome_completo(nome='Marina', sobrenome='Ruanna'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Ruanna', nome='Marina'))


# Erros comuns na utilização do return:

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num

    return total  # Lembrar que o return encerra a função, então em um loop deixar o return fora da função.


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

