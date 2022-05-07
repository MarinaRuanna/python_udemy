# coding=utf-8
"""
ESCREVENDO EM ARQUIVOS CSV

reader() (leitor)
writer() (escritor)

O método writer() cria um objeto que nos permite escrever em csv.

writerow() -> Escreve uma linha
"""

from csv import writer, DictWriter
'''
# writer():

# writer() -> Gera um objeto para que possamos escrever em arquivo CSV. Utilizamos o método writerow() 
para escrever cada linha. Este método recebe uma lista.

with open('filmes.csv',  'w', encoding='UTF-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow([filme, genero, duracao])
'''

# DictWrider:

# OBS: As chaves dos dicionário devem ser as mesmas utilizadas como cabeçalho.

with open('filmes3.csv', 'w', encoding='UTF-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow({"Título":filme, "Gênero": genero, "Duração": duracao})




