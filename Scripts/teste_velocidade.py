"""
TESTE DE VELOCIDADE COM EXPRESSÕES GERADORAS

"""
# Generators (Geradores):


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)   # Generator

print(next(ge1))
print(next(ge1))


# Generator Expression:

ge2 = (num for num in range(1, 10))

print(ge2)   # Generator Expression (genexpr)

print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade:
import time

# Generator Expression (mais rapido):

gen_inicio = time.time()
print(sum(num for num in range(1, 1000)))    # Mil

gen_tempo = time.time() - gen_inicio

# List Comprehension (mais lento):

list_inicio = time.time()
print(sum(num for num in range(1, 1000)))    # Mil
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehendion levou {list_tempo}')
