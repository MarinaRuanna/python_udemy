"""
LOOP FOR
loop -> Estrutura de repetição
for -> Uma dessas estruturas

C# ou Java

for(int i = 0; i < limitador; i++){
   //execução do loop
   }

# Python

for item in interavel:
    //execução do loop

Utilizamos loops para interar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:
 - string
     nome = marina ruanna
 - lista
     lista = [1, 3, 5, 7, 9]
 - range
     numero = range(1, 10)

nome = 'Marina Ruanna'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (iterando sobre uma string):
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista):
for numero in lista:
    print(numero)

# Exemplo de for 3 (interando sobre um range):
'''
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 -> não inclui
'''
for numero in range(1,10):
    print(numero)

'''
Enumerate:
((0, 'M'), (1, 'a'), (2, 'r'), (3, 'i'), (4, 'n'), (5, 'a'), (6, ' '), (7, 'R'), (8, 'u'), (9, 'a'), (10, 'n'), (11, 'n'), (12, 'a'))
'''
for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS:  Quando não precisamos de um valor, podemos descarta-lo usando o underline (_)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
   num = int(input(f'Informe o {n}/{qtd} valor: '))
   soma = soma + num
print(f'A soma é {soma}')

nome = 'marina ruanna'
for letra in nome:
    print(letra)


nome = 'marina ruanna'
for letra in nome:
    print(letra, end='')    # Print sem pular linha

Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F601
# Modificado: U0001F601

for _ in range(3):
   for num in range(1, 11):
       print('\U0001F601' * num)
"""












