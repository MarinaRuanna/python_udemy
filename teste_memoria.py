"""
TESTE DE MEMÓRIA COM GENERATOR

# TESTE:

for n in fib_lista(100000):
    print(n)

"""
# Sequencia de Fibonacci: 1, 1, 2, 3, 5, 8, 13...

# Função usando lisntas (491MB):


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando Generators (4.520MB):


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# TESTE:


for n in fib_gen(100000):
    print(n)



