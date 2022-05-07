"""
MÓDULO RANDOM - E o que são módulos.

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.
OBS: O modulo rabdom é um dos módulos integrados no Python que pode ser utilizando apenas o importando.
"""
# OBS: Existem duas formas de se utilizar um módulo ou função deste:

# FORMA 1 - Importando todo o módulo (Não recomendado):
'''
Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do 
módulo ficarão disponíveis (ficarão em memória). Caso vocÊ saoba quais funções você precisa utilizar deste módulo, 
então esta não seria a forma ideal de utilização. Veremos uma forma mais eficiente na forma 2
'''
import random

# random() -> Gera um número real aleatório entre o e 1

print(random.random())
'''
ATENÇÃO: Não confunda o pacote random com a função random(), pode parecer comfuso , mas a função random() 
é apenas uma função dentro do módulo random.

OBS: que para utilizar a função random() do pacote random, nos colocamos o nome do pacote e o nome da função separados por ponto (.).
'''

# FORMA 2 - Importanto uma função especifica do módulo (Forma recomendada):
from random import random # -> Do módulo random, importe a função random.

for i in range(10):
    print(random())

# uniform() -> Gera um numero real aleatório entre os números estabelecicidos.
from random import uniform

for i in range(10):
    print(uniform(7, 5))  # O útimo numero, nesse caso o número 7, não é incluído.

# randint() - > Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena:
for i in range(6):
    print(randint(1, 60), end=', ') # Começa em 1 e vai ate 60.


# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura', 'lagarto']

for i in range (2):
    print(choice(jogadas))

# shuffler() -> Tem a função de embaralhar dados.
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas)




