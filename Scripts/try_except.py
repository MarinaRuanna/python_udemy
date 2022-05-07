"""
TRY/EXCEPT

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo assim que o programa pare de funcionar e o usúario mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema
"""

# TRATANDO UM ERRO GENÉRICO:

# EXEMPLO 1:

try:
    geek()
except:
    print('Deu algum problema')
'''
Tente executar a função geek(), caso encontre erros, imprima a mensagem de erro.
'''

# EXEMPLO 2:
try:
    len(4)
except:
    print('Deu algum problema')
'''
OBS: Trata erros de forma genérica, não é a melhor forma de tratamento de erros. 
O ideal é sempre tratar de forma expecifica.
'''

# TRATANDO UM ERRO ESPECIFICO:

# EXEMPLO 1:
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# EXEMPLO 2 - Trantando um erro específico com detalhes do erro:
try:
    len(6)
except TypeError as err:
    print(f'A aplivação gerou o seguinte erro {err}')
'''
except TipoDoErro as err: capture uma exceção do tipo TipoDoErro e chame ela de err. 
'''

# EXEMPLO 3 - Tratando mais de um erro específico de uma vez:
'''
Podemos efetuar diversos tratamentos de erros de uma vez.
'''
try:
    len(5)
except NameError as err1:
    print(f'Deu NameError: {err1}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print('Deu um erro diferente')


try:
    geek()
except NameError as err1:
    print(f'Deu NameError: {err1}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print('Deu um erro diferente')


try:
    print('geek'[9])
except NameError as err1:
    print(f'Deu NameError: {err1}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print('Deu um erro diferente')


# EXEMPLO 4:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    except:
        return None


dict = {'nome': 'geek'}
print(pega_valor(dict, 'nome'))

dict = {'nome': 'geek'}
print(pega_valor(dict, 'game'))     # KeyError

dict = {'nome': 'geek'}
print(pega_valor(5, 'nome'))        # TypeError

