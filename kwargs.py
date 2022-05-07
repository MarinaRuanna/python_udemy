"""
ENTENDENDO **Kwargs

Poderiamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs.

Este é so mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados e transforma estes parÂmetros extras em um dicionário.

# EXEMPLO:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

#EXEMPLO MAIS COMPLEXO:
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

'''
Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs.
'''

# EXEMPLO - Ordem dos parâmetros:

def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome.title()} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro.')
    else:
        print('Casado')
    print(kwargs)

minha_função(8, 'julia')
minha_função(18, 'felicity', 4, 5, 3, solteiro=True)
minha_função(34, 'felipe', eu='Não', voce='vai')
minha_função(19, 'carla', 9, 4, 3, java=False, Python=True)


minha_função(29, 'marina', 'Estudante', solteiro=True, escolaridade='graduação')

# Entenda por quê é importante manter a ordem dos parâmetros na declaração:

# Função com a ordem CORRETA dos parâmetros:
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

'''
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor
'''
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Função com a ordem INCORRETA de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, instrutor, args, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs:
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Marina', 'sobrenome': 'Ruanna'}

# print(mostra_nomes(nomes)) #TypeError

print(mostra_nomes(nome='Marina', sobrenome='Ruanna'))

# Simplificando com o duplo asterisco:

print(mostra_nomes(**nomes))


# EXEMPLO:
def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(1, 2, 3)
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

'''
OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função.

dicionario = dict(d=1, e=2, f=3) #TypeError
soma_multiplos_numeros(**dicionario)
'''

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')
"""