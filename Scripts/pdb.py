"""
DEBUGGANDO COM PDS

PDB -> Python Debugger

Bug -> Inseto
"""

# EXEMPLO 1 - RUIM -> A utilização do print() para debbugar o código é uma pratica RUIM:
def dividir(a, b):
    print(f' a = {a}, b = {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'

print(dividir(4, 7))


'''
Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger.
Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB - Python Debugger.
'''

# EXEMPLO -PyCharm:
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# EXEMPLOS - PDB - Python Debbuger:
'''
Para utilizar o PYthon Debugger, precisamos*, importar a biblioteca PDB e então utilizar a função set_trace()

COMANDOS BÁSICOS PDB:
- l (lista onde estamos no código)
- n (próxima linha)
- p (imprime variável)
- c (Continua a execução - finaliza o debugging)

'''

# EXEMPLO 1:
import pdb

nome = 'Marina'
sobrenome = 'Ruanna'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)


# EXEMPLO 2:
'''
OBS: O debug é utilizado durante o desenvolvimento, costumamos realizar todos os impots de bibliotecas no inicio 
do arquivo. Por isso, ao invés de colocar o import PDB no início do arquivo, nos colocamos somente onde vamos debuggar, 
e ao finalizar ja a remoção.
'''
nome = 'Marina'
sobrenome = 'Ruanna'
import pdb; pdb.set_trace()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)


# EXEMPLO 3:
'''
* A partir do Python 3.7, não é mais necessário importar a biblioteca PDB, pois o comando de debug foi incorporado 
como função integrada (Built in) chamada breakpoint()
'''
nome = 'Marina'
sobrenome = 'Ruanna'
breakpoint()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)


#  EXEMPLO 4:
'''
ATENÇÃO: Cuidados com comflitos entre os nomes de variáveis e os comandos PDB:
'''
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

''' 
Neste caso, como os nomes das variáveis sao os mesmos dos comandos PDB, devemos utilizar o comando p para imprimir as variáveis, 
ou seja, p nome_da_variável.
'''
'''
Não devemos utilizar nomes não reprsentativos nas variáveis. 
Sempre optar por nomes significativos.
'''

# Refatorando o exemplo 4:

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4