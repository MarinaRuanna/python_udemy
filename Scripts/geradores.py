"""
GENERATORS (geradores)

- Generators (geradores) são iteretors (iteradores);

OBS: O contrário não é verdadeiro, ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criador com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras.

Diferenças entre Funções e Generators Functions (funções geradoras):
__________________________________________________________________________________________
/Funções                                     / Generators Functions                      /
------------------------------------------------------------------------------------------
/ Utilizam return                           / Utilizam yield                             /
------------------------------------------------------------------------------------------
/Retorna uma vez                            / Pode utilizar yield multiplas vezes        /
------------------------------------------------------------------------------------------
/Quando executada, retorna um valor         /Quando executada, retorna um generator      /
------------------------------------------------------------------------------------------

"""
# EXEMPLO - Generator Function (Função Geradora):


def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


'''
OBS: Uma Generator Function não é um Generator, ela gera um Generator.
'''

gen = list(conta_at(10))

print(gen)

for num in gen:
    print(num)



