"""
TRY, EXCEPT,  ELSE, FINALLY

Dica de quando e onde usar tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é destruir seu sistema.
"""

# EXEMPLO - else -> Só é executado se não ocorrer nenhum erro:

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor inválido.')
else:
    print(f'Você digitou o {num}')

# EXEMPLO 1 - finally -> O bloco finally é SEMPRE executado independente se houve exceção ou não.
'''
O finally, geralmente é utilizado para fechar ou desalocar recursos.
'''
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# EXEMPLO - Mais complexo - Tratando de modo ERRADO:
'''
Criando uma função que receba dois valores e retorne a divisão de um valor pelo outro:
'''
def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número:'))
try:
    num2 = int(input('Informe o segundo número:'))
except ValueError:
    print('O valor precisa ser númerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor invalido')



# EXEMPLO - Mais complexo - Tratando de modo CORRETO:
# OBS: Você é responsável pelas entradas das suas funções, então trate-as:
'''
Criando uma função que receba dois valores e retorne a divisão de um valor pelo outro:
'''

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
       return 'Valor inválido.'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# EXEMPLO - Tratamento genérico:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
       return 'Ocorreu um erro'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# EXEMPLO - Tratamento semi-genérico:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))