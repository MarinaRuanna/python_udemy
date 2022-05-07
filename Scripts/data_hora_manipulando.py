"""
MANIPULANDO DATA E HORA

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

"""

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# O módulo datetime possui um método datetime

# datetime.datetime.now retorna a data e hora corrente:
print(datetime.datetime.now()) # 2022-03-08 15:36:22.646488

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# repalce() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)


# Recebendo dados do usuário e convertendo para data::

nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')

print(type(nascimento))

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

# Acessa individual dos elementos de uma data e hora:

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))

