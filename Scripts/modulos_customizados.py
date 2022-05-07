"""
MÓDULOS CUSTOMIZADOS

Como os módulos Python nada mais são do que arquivos Python,
então TODOS os arquivos que criamos neste curso são módulos Python prontos para serem utilizados."""

# EXEMPLO:

from testes import (
    soma_impares,
    nome_completo
)

print(nome_completo('Marina', 'Ruanna'))

print(soma_impares(1, 2, 6, 9, 15, 84))



'''
ATENÇÃO: Se houver funções print() definidas no módulo (arquivo) que você importou,
eles irão aparecer ao executar a função.
'''