"""
PEP8 - Python enhacemente proposal
(Propostas de melhorias para a linguagem Python)
import this
The Zen of Python
A ideia da PEP8 é que possamos escrever codigos Python de forma Pythônica

[1.] - Utilize camel case para nomes de classes:
[2.] - Ultilize nomes em minúsculo, separados por underline para funções ou variáveis
[3.] - Ultilize 4 espaços para identação! (NÃO é recomendado usar tab)
[4.] - Linhas em branco
          - Separar duas funções e definições de classe com duas linhas em branco;
          - Métodos dentro de uma classe devem ser ser separados com uma única linha em branco;

[5.] - Imports devem ser sempre feitos em linhas separadas
           # import errado:
           import sys, os

           #import certo
           import sys
           import os      >>>> Para pacotes completos

  - Não há problemas em ultilizar:
     from types import StringTypes, ListType >>>> Pra classes em pacotes

  - Caso tenha muitos imports de um mesmo pacote, recomenda-sefazer:

  from types import (
    StringType
    ListType
    OutroType
)

  - Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentário ou docstrings e antes de constantes ou variáveis globais

[6.] - Espaços entre expressões e instruções:
   Exemplo 1:
     NÃO FAÇA:
      funcao( algo[ 1 ], {outro: 2 } )

     FAÇA:
      funcao(algo[1], {outro: 2})

   Exemplo 2:
     NÃO FAÇA:
      algo (1)

     FAÇA:
      algo(1)

   Exemplo 3:
     NÃO FAÇA:
      dict ['chave'] = list [indice]

     FAÇA:
      dict['chave'] = list[indice]

   Exemplo 4:
     NÃO FAÇA:
      x              = 1
      y              = 3
      variavel_longa = 5

     FAÇA:
     x = 1
     y = 3
     variave_longa = 5

[7.] - Termine sempre uma instrução como uma nova linha
"""
print("Run ok!")
