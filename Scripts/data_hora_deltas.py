"""
TRABALHANDO COM DELTAS DE DATA E HORA (diferenças entre datas e horas)

data_inicial = dd/mm/aaaa 12:55:34.9939392
data_final = dd/mm/aaaa 13:34:23.0948484

delta = data_final - data_inicial
"""

import datetime

# Temos a data de hoje:
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2022, 5, 24, 0)

# Calculando o delta:
tempo_para_o_evento = aniversario - data_hoje

print(type(tempo_para_o_evento))

print(repr(tempo_para_o_evento))

print(tempo_para_o_evento)

print(f'faltam {tempo_para_o_evento.days} dias, {(tempo_para_o_evento.seconds // 60) // 60} horas...')

# EXEMPLO 1:

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_compra + regra_boleto

print(vencimento_boleto)