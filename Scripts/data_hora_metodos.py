"""
MÉTODOS DE DATA E HORA


# Com now() podemos especificar um timezone (Fuso Horário):
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
"""

import datetime

# Mudanças ocorrendo á meia-noite -> combine():

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana -> weekday():

'''
Os dias da semana do método weekday() começam em zero, sendo está a segunda-feira:

0 - Segunda-feira (Monday)
1 - Terça-feira   (Tuesday)
2 - Quarta-feira  (Wednesday)
3 - Quinta-feira  (Thursday)
4 - Sexta-feira   (Friday)
5 - Sábado        (Saturday)
6 - Domingo       (Sunday)
'''

print(manutencao.weekday()) # 5 -> Sábado

aniversario = input('Informe sua data de nascimento (dd/mm/aaa): ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

print(aniversario)

print(aniversario.weekday())

if aniversario.weekday() == 0:
    print('Você nasceu em uma Segunda-feira!')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-feira!')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta-feira!')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-feira!')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-feira!')
elif aniversario.weekday() == 5:
    print('Você nasceu em um Sábado!')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo!')

# Formatando datas/horas com strftime() (String Format Time):
# dd/mm/aaaa hora:minuto

'''
def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado= hoje.strftime('%d de %B de %Y')   # %Y aaaa -> %y aa   //  %m numero do mês  -> %B  nome do mês

print(hoje_formatado)

print(formata_data(hoje))
'''

# Refatorando a função:

from textblob import TextBlob
# https://textblob.readthedocs.io/en/dev/

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))

# Transformando uma string em um objeto do tipo datetime -> strptime()

# Recebe uma string e o formato dela:
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

# EXEMPLO:
aniversario = input('Qual sua data de nascimento (dd/mm/aaaa): ')

aniversario = datetime.datetime.strptime(aniversario, '%d/%m/%Y')

print(type(aniversario))

print(nascimento)


# Somente a hora:

almoco = datetime.time(12, 30, 0)

print(almoco)

# Marcando tempo de execução do nosso código com timeit:

import timeit, functools

# Loop for:
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print(tempo)

# List Comprehension:
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(tempo)

# Map:
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000)
print(tempo)

# Testando timeit em uma função:

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))




