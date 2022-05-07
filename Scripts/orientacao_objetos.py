"""
ORIENTAÇÃO Á OBJETOS

Paradigmas de Programação: - Forma/Metodologia utilizada para pensar/desenvolver sistemas.
- Programação estruturada:
    - Linguagens: Python, C
- Programação orientada a objetos:
    - Linguagens: Python, Java
- Programação funcional:
    - Linguagens: Python

OBS: O Python é considerada uma linguagem multiparadigma.


O objetivo da programação orientada a objetos é mapear objetos do mundo real para modelos computacionas,
fazendo com que possamos facilmente representar tais objetos com suas caracteristicas e comportamentos.

Principai elementos da Orientação á Objetos:
- Classe -> Modelo de objeto do mundo real sendo representado computacionamente.
- Atributo -> Características do objeto.
- Método -> Comportamento do objeto (funções).
- Construtor -> Método especial utilizado para criar objetos.
- Objeto -> Instacia da classe.
"""

numero = 10
print(numero)
print(type(numero))

nome = 'Marina'
print(nome)
print(type(nome))

class Produto:
    pass

ps4 = Produto()
print(ps4)
print(type(ps4))

