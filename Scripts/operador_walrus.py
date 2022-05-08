"""
OPERADOR WALRUS

O operador Walrus permite fazer a atribuição e retorno do valor em uma única expressão.

variavel := expressão
"""

# EXEMPLO:

print(nome := "Geek University")

# EXEMPLO 2:
'''
cesta = []
fruta = input("Informe a fruta: ")

while fruta != 'sair':
    cesta.append(fruta)
    fruta = input("informe a fruta: ")
'''

# PYTHON 3.8:

cesta = []

while (fruta:= input('Informe a fruta: ')) != 'sair':
    cesta.append(fruta)

