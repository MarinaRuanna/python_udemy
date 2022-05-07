# coding=utf-8
"""
ESCREVENDO ARQUIVOS EM CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula:

1, 2, 3, 4, 5

"geek", "university", "python", "ciência", "dados

# Separador por ponto e vírgula:

1; 2; 3; 4; 5

"geek"; "university"; "python"; "ciência"; "dados

# Separador por espaço:

1 2 3 4 5

"geek" "university" "python" "ciência" "dados

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso):

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
 #  print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possuí duas formas diferentes para se ler dados em arquivos CSV:
    - reader -> Permite que íteremos sobre as linhas do arquivo CSV
    - DictReader -> Permite que íteremos sobre as linhas do arquivo CSV como OrderedDicts
"""
from csv import reader, DictReader

# Reader:
with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}')



# DictReader:
with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é um OrdereDict
        print(f"{linha['Nome']} nasceu no(a) {linha['Pais']} e mede {linha['Altura (em cm)']}")

3

# DictReader - Com outro separador:
with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é um OrdereDict
        print(f"{linha['Nome']} nasceu no(a) {linha['Pais']} e mede {linha['Altura (em cm)']}")
