"""
FUNÇÕES VOM PARÂMETRO PADRÃO (Default Parameters)

- Funções onde a passagem de parâmetros seja opcional;
"""
# Exemplo de função onde a passagem de parâmetro seja opcional:

print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória (TypeError):


def quadrado(numero):
    return numero ** 2


print(quadrado(9))
print(quadrado()) # TypeError


def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3))    # Por padrão eleva ao quadrado.
print(exponencial(3, 5)) # Eleva á potencia informada pelo usuário.

'''
OBS: Se o usuário passar somente 1 argumento, este será atribuido ao parâmetro numero e será calculado o
quadrado deste número. Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao
parâmetro potencia. Então será calculada esta potência.
'''

print(exponencial())

# OBS: Em funções Python, os parâmetros com valores padrão (default), DEVEM sempre estar ao final da declaração.
'''
# ERRO!
def teste(num=2, potencia):   # SymtaxError
    return num ** potencia
'''
print(teste(6))

# CORRETO!
def teste(num, potencia=2):
    return num ** potencia

print(teste(6))

# Outros exemplos:
def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo:
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor.'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Marina'))
print(mostra_informacao(nome='Ruanna'))
print(mostra_informacao('Geek', True))
'''
# Por que utilizar parametros com valor default (padrão)?

- Nos permitem ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de códigos.

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dados:
    - Números
    - Strings
    - Floats
    - Booleanos
    - Listas
    - Tuplas
    - Dicionários
    - Funções
    - Etc.
'''
# EXEMPLO - Função como parâmetro:
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões:

# Variáveis globais;
# Variáveis locais;

instrutor = 'Geek'        # Variável global

def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}!'

print(diz_oi())
'''
OBS: Se tivermos uma variável local com o mesmo nome de uma variavel global, ela terá preferencia,
ou seja, ela será utilizada.
'''

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Oi {prof}!'

print(diz_oi())

print(prof) # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local esta sendo usada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# Corrigindo o erro:

total = 0

def incrementa():
    global total      # Avisando que queremos utilizar a variável global.

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável:

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro()) # NameError



