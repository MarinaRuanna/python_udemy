"""
ARGUMENTOS SOMENTE POSICIONAIS -> (/)

Não se nomeia o argumento
"""

valor = '67.3'
print(float(valor))

def cumprimenta_v1(nome):
    return f'Olá {nome}!'

print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))

def cumprimenta_v2(nome, /):
    return f'Olá! {nome}!'

print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))

def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem}! {nome}!'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem}! {nome}!'

print(cumprimenta_v4('Geek'))
print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('University', mensagem='Hello'))


def cumprimenta_v5(*, nome):
    return f'Hello! {nome}!'

print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Felicity'))

def cumprimenta_v6(nome, /, mensagem='Olá!', *, mensagem2):
    return f'{mensagem}! {nome}! {mensagem2}'

print(cumprimenta_v6('Geek', mensagem='Hello', mensagem2='Tenha um bom dia!'))
print(cumprimenta_v6('Geek', mensagem2='Tenha um bom dia!'))
# print(cumprimenta_v6('Geek', 'Hello', 'Tenha um bom dia!'))
