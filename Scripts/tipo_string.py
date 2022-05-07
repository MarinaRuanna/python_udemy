"""
TIPO STRING
"""

# Em Python, um dado é considerado do tipo string sempre que:
# - Estiver entre áspas simplis -> 'uma string', '2,3,4', 'a', 'True', '42,3'
# - Estiver entre áspas duplas -> "uma string", "2,3,4", "a", "True", "42,3"
# - Estiver entre áspas simples triplas -> '''uma string''', '''2,3,4''', '''a''', '''True''', '''42,3'''
# - Estiver entre áspas duplas triplas -> """uma string""", """2,3,4""", """a""", """True""", """42,3"""
"""
O mais comum no tipo string é o uso de áspas simples
"""

nome = 'Marina Ruanna'
print(nome)
print(type(nome))

nome = "'Marina's Bar"
print(nome)
print(type(nome))

nome = 'Marina \nRuanna'
print(nome)
print(type(nome))

nome = 'Marina \" Ruanna'
print(nome)
print(type(nome))

nome = """Marina
Ruanna"""
print(nome)
print(type(nome))

nome = 'Marina Ruanna'
print(nome.upper())
print(type(nome))

nome = 'Marina Ruanna'
print(nome.lower())
print(type(nome))

nome = 'Marina Ruanna'
print(nome.split()) # Transforma em uma lista de strigs
print(type(nome))
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12]
# ['M', 'a', 'r', 'i', 'n', 'a', ' ', 'R', 'u', 'a', 'n', 'n', 'a']
nome = 'Marina Ruanna'
print(nome[0:6]) # Slice de string

print(nome[7:13]) # Slice de string

print(nome[7:12+1]) # Slice de string

print(nome.split())
# [    0,       1]
# ['Marina', 'Ruanna']
print(nome.split()[1])

"""
[::-1] -> Comece do primeiro elemento, vá atá o último elemento e inverta.
"""
print(nome[::-1]) # Inversão da string

print(nome.replace('a', 'i'))

# Palindromo
texto = 'socorram me subino onibus em marrocos'
print(texto[::-1])






