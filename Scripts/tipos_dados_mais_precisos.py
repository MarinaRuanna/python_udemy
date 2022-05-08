"""
TIPOS DE DADOS MAIS PRECISOS
"""

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro('Geek ')) #mypy: "str"; expected "int" Found 1 error in 1 file (checked 1 source file)

'''
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols
'''

# Literal Type:

from typing import Literal

def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

# Sem o Literal:
def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} + {num2} = {num1- num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)
calcula_v1('-', 18, 2)
# calcula_v1('*', 3, 5)


# Com o Literal:
def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} + {num2} = {num1- num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')

calcula_v2('+', 6, 4)
calcula_v2('-', 18, 2)
# calcula_v2('*', 3, 5)


# Union:

from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado

print(soma(2, 3))

# Final:

from typing import Final
from typing import final

NOME: Final = 'Geek'

print(NOME)

NOME = 'University'

print(NOME)


# final como decorador:

@final
class Pessoa:
    pass

class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')

class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudndo e estagiando...')


# Typed Dictionaries:

from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='Vai', coisa=True)

print(outro)

# Protocols:

from typing import Protocol

class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')

class Venda:
    titulo = 'Programação em Python'

v1 = Venda()

estudar(v1)
