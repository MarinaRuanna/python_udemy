"""
TRABALHANDO COM MÓDULOS BUIT-IN

Módulos Built-in -> Módulos que já vem instalados no Python.
________________________
|Python|Módulos builtin| -> Ao instalar o Python.
------------------------

https://docs.python.org/3/py-modindex.html
"""

# Podemos importar todas as funções de um módulo utilizando o asterisco (*):

from random import *

print(random())
'''
OBS: Fazendo o import de todas as funções do módulo desta maneira, não se faz necessário usar o módulo.função(), 
a exemplo de: random.random()
'''

# Utilizando alias (apelidos) para módulos/função

# EXEMPLO - Apelidos para módulos:
import random as rdm # Dando um apelido ao módulo random.
print(rdm.random())

# EXEMPLO - Apelidos para funções:
from random import randint as rdi, random as rdm

print(rdi(5, 10))

print(rdm())

'''
ATENÇÃO: Não devemos utilizar nomes de outras funções builtins como apelido, e também nomes de variáveis que estão 
sendo utilizadas.
'''

# Fazendo múltiplos imports de um mesmo módulo::
'''
Forma Pythônica: Nestes casos costumamos utilizar tuple para colocar mútiplos imports de um mesmo módulo.
'''
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(1, 10))

lista = ['Geek', 'University', 'Python']
print(shuffle(lista))

print(choice('University'))
