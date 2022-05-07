"""
LISTAS (list)

Lista em python funcionam como vetores/matrizes (arrays, em outras linguagens), com a diferença de serem dinamicos e podermos colocar QUALQUER tipo de dado.

lINGUAGENS C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nessas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no maximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo, podemos criar a lista e simplismente ir adcionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.
- Listas são mutaveis, elas podem mudar constantemente.

As listas em Python são representadas por: []
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = [ 'm', 'a', 'r','i', 'n', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('marina')

# Podemos facilmente checar se determinado valor esta contido na lista:
num = int(input('Digite um numero inteiro: '))
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')


# Podemos facilmente ordenar uma lista:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista1.sort()
print(lista1)

lista5 = list('marina')

lista5.sort()
print(lista5)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista:
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em listas:

'''
Para adicionar elementos/valores em listas utilizamos a função append()
'''
print(lista1)
lista1.append(42)
print(lista1)
lista1.sort()
print(lista1)

# OBS: Com append nos no sonseguimos adicionar 1 elemento/valor por vez
# lista1.append(12, 34, 56) -> OCORRE ERRO

lista1.append([8, 3, 1])  # Coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adcional a lista
print(lista1)


# Pdemos inserir um novo elemento na lista informando a posição do indice:
# OBS: Isso não substitui o valor inicial, o mesmo será delocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)


# Podemos facilmente juntar 2 listas:
# lista6 = lista1 + lista2 OU;
# lista1 = lista1 + lista2 OU;
# lista1.extend(lista2)
print(lista1)
# print(lista6)

# Podemos facilmente inverter uma lista:
# Forma 1:
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Forma 2:
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista:
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista:
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista:
print(lista5)
lista5.pop()
print(lista5) # OBS: O pop não so mente remove o ultimo elemento mais também o retorna


# Podemos remover um elemento pelo indice:
# OBS 1: Os elementos a direita deste indice serão deslocados para a esquerda.
# OBS 2: Se não houver elemento no indice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)


# Podemos facilmente remover todos os elementos, ou seja, zerar a lista:
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista:
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista:

# Exemplo 1:
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split() # OBS: Por padrão, o split separa os elementos da lista pelos espaços entre elas.
print(curso)

# Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)



# Convertendo uma lista em uma string:
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista 6, coloca cifrão ($) entre cada elemento e transforma em uma string.

curso = '$'.join(lista6)
print(curso)


# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados:
lista6 = [1, 2.34, True, 'marina', 'm', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))


# Iterando sobre listas:

# Exemplo 1(utilizando o for):
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 (utilizando while):
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando variaveis em listas:
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada:
#         0        1      2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print (cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
'''
Fazer os acessos de forma indexada reversa:
Para entender melhor o indice negativo, pense na lista como um circulo,
onde o final de um elemento esta ligado ao incicio da lista
'''

# Gerar indice em um for:
for indice, cor in enumerate(cores):
     print(indice, cor)


# listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# Outros métodos não tão importantes mas também uteis:
# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista o valor 6:
print(numeros.index(6))

# Em qual indice da lista o valor 9:
print(numeros.index(9))

# Caso nao tenha esse elemento na lista, será apresentado erro, ValueError

print(numeros.index(5)) # Retorna o indice do primeiro ele,emto encontrado.

# Podemos fazer busca dentro de um range, ouseja, qual indice a buscar.
print(numeros.index(5, 1)) # Buscando a partir do indice 1
print(numeros.index(5, 2)) # Buscando a partir do indice 2
print(numeros.index(5, 3)) # Buscando a partir do indice 3
print(numeros.index(5, 4)) # Buscando a partir do indice 4 -> ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o indice do valor 8 entre os indices 6 a 8

# Revisão de slicing:

# lista[inicio:fim:passo]
# range(inicio:fim:passo]

# Trabalhando com slice de lista com parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parametro 'fim'

print(lista[:2]) # Começa em 0, pega ate o indice 2 - 1
print(lista[:4]) # Começa em 0, pega ate o indice 4 - 1
print(lista[1:3]) # Começa em 1, pega ate o indice 3 - 1

# Trabalhando com slice de lista com parametro 'passo':

print(lista[1::2]) # Começa em 1, vai ate o final de 2 em 2.
print(lista[::2])  # Começa em 0, vai ate o final de 2 em 2.


# invertendo valores em uma lista:

nomes = ['marina', 'ruana']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['marina', 'ruana']
nomes.reverse()
print(nomes)


# Soma*, Valor maximo*, Valor minimo*, Tamanho
# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # valor maximo
print(min(lista)) # valor minimo
print(len(lista)) # tamanho da lista


# Podemos transformar uma lista em tupla:

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de lista
lista = [1, 2, 3,]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

'''
OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados, teremos ValueError.
'''

# Copiando uma lista para outra (Shallow Copy e Deep Copy):

# Forma 1 (Deep Copy):

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

'''
Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente 
independentes, ou seja, modificando uma lista, não afeta a outra. isso em Python, é chamado de Deep Copy (copia profunda).
'''


# Forma 2 (Shallow Copy):

lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)

'''
Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas apos realizar modificação
 em uma das listas, essa modificação se refletiu em ambas as listas, isto em Python é chamado de Shallow Copy.
'''

