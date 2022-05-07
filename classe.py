"""
POO - CLASSES

Em POO, Classes nada mais são do que modelos dos objetos do mundo real, sendo representados computacionalmente.


Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa:
Classe podem conter:

    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lampada por exemplo, iriamos querer saber se a
    lampada é, 110 volts ou 220 volts, se ela é branca, amarela, vermelha ou outra cor,
    se está ligada ou deligada, qual a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no
    sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente
    iriamos querer representar no nosso sistema é o ligar e desligar a mesma.

Em Python para definirmos uma classe, usamos a palavra reservada class.

Usamos a palavra reservada 'pass' em Python quando temos um bloco de código que ainda não esta implementado.

OBS: Quando nomeamos nossas uma classe em Python, utilizamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

OBS: Em computação, não utilizamos: Acentuação, caracteres especiais, espaços ou similarespara nomes de classes,
atributos, métodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mapeados para a classe de entidade.
"""

idade = 32               # tipo int

preco = 2340.45          # tipo float

nome = 'Marina Ruanna'   # string

class Lampada:
    pass

lamp = Lampada()

print(type(lamp))        # tipo Lampada

class ContaCorrente:
    pass

class Produtos:
    pass

class Usuario:
    pass



