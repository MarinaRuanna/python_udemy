"""
PRESERVANDO METADATAS COM WRAPS

Metadados - São dados intrísecos em arquivos.

Wraps - São funções que envolvem elementos com diversas finalidades.
"""

# PROBLEMA:

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


print(soma.__name__)     # soma
print(soma.__doc__)      # Soma dois números

'''
No caso acima o nome da função e a documentação apresentadas pertencem a Decorator Function, e não a função soma, 
podendo causar confusão ao se coonsultar os metadados.
'''

# RESOLUÇÂO:

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print(soma(10, 30))
print(soma.__name__)     # soma
print(soma.__doc__)      # Soma dois números




