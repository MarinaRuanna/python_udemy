"""
Recebendo dados do usuario:

 - Entrada de dados:
     print("Qual o seu nome?")
     nome = input()          Input -> Entrada

 - Processamento

 - Saida de dados:
    print(f'Seja bem-vindo(a) {nome}')

 - Entrada de dados:
     print("Qual a sua idade?")

 - Processamento
     idade = input()

 - Saida de dados
     print(f'A {nome} tem {idade} anos')


#EXEMPLO DE PRINT ANTIGO:

print("Qual o seu nome?")
nome = input()
print('Seja bem - vindo(a)%s' % nome)

print("Qual a sua idade?")
idade = input()
print('A %s tem %s anos' % (nome, idade))


# EXEMPLO DE PRINT MODERNO:

print("Qual o seu nome?")
nome = input()

print("Qual a sua idade?")
idade = input()

print('Seja bem vindo(a) {0}'.format(nome))
print('A {0} tem {1} anos'.format(nome,idade))

# EXEMPLO DE PRINT MAIS ATUAL:

print("qual o seu nome?")
nome = input()

print(f'Seja bem-vindo(a) {nome}')

print("Qual a sua idade?")
idade = input()

print(f'A {nome} tem {idade} anos')

# EXEMPLO INPUT SIMPLIFICADO:
nome = input("Qual o seu nome?")
print(f'Seja bem-vindo(a) {nome}')
idade = input("Qual a sua idade?")
print(f'A idade do(a) {nome} é {idade}')
print(f'O(a) {nome} nasceu em {2021 + int(idade)}')

"""

nome = input("Qual o seu nome?")

print(f'Seja bem-vindo(a) {nome}')

idade = int(input("Qual a sua idade?"))

print(f'A idade do(a) {nome} é {idade}')

print(f'O(a) {nome} nasceu em {2021 - idade}')
""" 
int(idade) => cast
cast é uma conversão de um tipo de dado para outro tipod e dado.

Todo dado recebido via input é do tipo string"""

# Em python, string é tudo que estiver em:
# Aspas simples:
# Apas duplas:
# Aspas simples triplas:
# Aspas duplas triplas:

# EXEMPLOS:
  # Aspas simples: 'Marina Ruanna'
  # Aspas duplas: "Marina Ruanna"
  # Aspas simples triplas: '''Marina Ruanna'''
  # Aspas duplas triplas: """ Marina Ruanna """ """








