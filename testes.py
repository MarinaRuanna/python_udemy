
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c



def quadrado_de_sete():
    return 7 * 7

def quadrado(numero):
    return numero ** 2


def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) *msg

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}.'

def soma_impares(numero):
    total = 0
    for num in numero:
        if num % 2 != 0:
            total = total + num
    return total  # Lembrar que o return encerra a função, então em um loop deixar o return fora da função.