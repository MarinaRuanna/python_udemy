"""
SISTEMA DE ARQUIVOS - NAVEGAÇÃO


Para fazer uso de manipulacao de arquivos do sistema operacional, precisamos importar e fazer uso do modulo os.

os -> Operation System - Sistema Operacional
"""

# Fazer o import:

import os

# getcwd() -> Pega o corrent work diretory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd())

# Para mudar o diretorio, podemos utilizar o chdir():

os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretorio e absoluto ou relativo:

print(os.path.isabs('/home/geek'))  # False ou True

# OBS.: Para usuarios Windows, se voce infelizmente estiver utilizando um computador com windows, tera que ter cuidado ao verificar diretorio.

print(os.path.isabs('C:\\User\\geek'))  # False ou True

# Podemos identificar o sistema operacional com o modulo os:

print(os.name)  # Posisx - Linux e Mac  # nt - Windows

# Podemos ter mais detalhes no sistema operacional:

print(os.uname())

# Fazer o import

import sys

print(sys.plataform)

print(os.getcwd())

res = os.path.join(os.getcwd(), 'nome do diretorio')
os.chdir(res)

print(os.getcwd())

'''
Veja que o os.patch.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o diretorio que sera juntado ao atual.
'''


# Podemos listar os arquivos e diretorios o listdir():

print(os.listdir)  # Lista os diretorios

print(len(os.listdir))  # Quantidade de diretorios

# Podemos listar os arquivos e diretorios com mais detalhes com o scandir():

print(os.scandir('\\nome do diretorio'))

print(list(os.scandir('\\nome do diretorio')))

arquivos = os.scandir('\\nome do diretorio')

print(arquivos)

print(dir(arquivos[0]))


scanner = os.scandir

arquivos = list(scanner)

print(dir(arquivos[0].inode()))
print(dir(arquivos[0].name()))       # Nome do arquivo
print(dir(arquivos[0].is_dir()))     # True ou False (tratasse de um diretorio?)
print(dir(arquivos[0].is_file()))    # True ou False (tratasse de um arquivo?)
print(dir(arquivos[0].is_symlink())) # True ou False (tratasse de link simbolico?)
print(dir(arquivos[0].patch))        # Caminho ate o arquivo
print(dir(arquivos[0].stat()))       # Estatisticas sobre o arquivo

# OBS.: Quando utilizamos a funcao scardir() nos precisamos fecha-la, assim como quando abrimos um arquivo:

scanner.close()
