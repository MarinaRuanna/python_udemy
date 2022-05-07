"""
TIPO FLOAT

Tipo real, decimal
Casas decimais: A separação das casas decimais é feita com ponto (.) e não com virgula (,).

"""
# ERRADO DO PONTO DE VISTA DO FLOAT, MAS GERA UMA DUPLA
valor = 1,44
print(valor)
print(type(valor))

# CERTO DO PONTO DE VISTA FLOAT
valor = 1.44
print(valor)
print(type(valor))

# É POSSIVEL FAZER DUPLA ATRIBUIÇÃO
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# PODEMOS CONVERTER UM FOAT PARA UM INT (inteiro)
"OBS: Ao converter valores float para inteiro, nõs perdemos precisão"
resultado = int(valor)
print(resultado)
print(type(resultado))

# PODEMOS TRABALHAR COM NUMEROS COMPLEXOS
variavel = 5j
print(type(variavel))
print(variavel ** 2)




