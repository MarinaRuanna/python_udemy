"""
SISTEMA DE ARQUIVOS - MANIPULACAO

Modulo os:
https://docs.python.org/3/library/os.html#module-os
"""
import os

# Descobrindo se um arquivo e/ou diretorio ja existe:

# Arquivos:
print(os.path.exists('frutas.txt'))   # True

print(os.path.exists('arquivo.txt'))  # False

# Diretorios:

# Paths relativos
print(os.path.exists('Geek'))

print(os.path.exists('Geek\\University\\arquivo.py'))

# Paths absolutos:
print(os.path.exists('C:\\User\\Geek\\University\\arquivo.py'))

# Criando arquivos:

# FORMA 1:
open('arquivo.teste.txt', 'w', encoding='UTF-8').close()

# FORMA 2:
open('arquivo.teste2.txt', 'a', encoding='UTF-8').close()

# FORMA 3:
with open('arquivo.teste3.txt', 'w', encoding='UTF-8') as arquivo:
    pass     # Não faz nada. Simplismente fecha o bloco.

# FORMA 4:
os.mknod('arquivo.teste4.txt')

os.mknod('C:\\Users\\Miguel\\Desktop\\Backup Marina\\arquivo.teste5.txt')

# OBS: Criando um arquivo com mknod(), se o arquivo já existir teremos um erro FileExistsError

# Criando diretórios - únicos (um a um):

# Path relativo:
os.mkdir('templates')

# Path absoluto:
os.mkdir('C:\\Users\\Miguel\\Desktop\\Backup Marina\\templates')

# A função mkdir() cria um diretório se este não existir. Caso Exista, teremos um File ExistsError.
# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError.

# Criando diretórios - mútiplos (árvore de diretórios):

os.makedirs('templates/geek/university')

# OBS: Se já existir teremos um erro FileExistsError

# Se o arquivo já existir, ele simplismente ignora:
os.makedirs('templates2/geek2/university2', exist_ok=True)

# Renomeando arquivos e diretórios:

# Diretórios:
os.rename('templates', 'geek')

# OBS: Se o diretório não existir, teremos um FileNotFoundError.
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError.

# Arquivos:
os.rename('C:\\Users\\Miguel\\Desktop\\Backup Marina\\arquivo.teste5.txt', 'C:\\Users\\Miguel\\Desktop\\Backup Marina\\geek.txt')

os.rename('texto.txt', 'geek.txt')


# Renovendo arquivos:
'''
ATENÇÃO: Tome cuidado como os comandos de deleção. Ao deletarmos um arquivo ou diretório, 
eles não vao para a lixeira, eles SOMEM.
'''
os.remove('nome_arquivo.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotExistsError
# OBS: Se você informar um diretório ao invés de um arquivo, teremos u, IsADirectoryError

# Removendo diretórios vazios:
os.rmdir('nome_diretorio')

# OBS: Se o diretóirio tiver qualquer conteúdo teremos um OSError.
# OBS: Se o diretório não existir teremos um FileNotFoundError


# Removendo multiplus arquivos:
for arquivo in os.scandir('nome_diretório'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podem,os remover uma árvore de diretórios vazios:
os.removedirs('nome_diretorio/outro/mais')

# OBS: Se algum dos diretórios tiver arquivos ou outros diretórios, o processo para
'''
ATENÇÃO: AO Remover arquivos e diretórios com Python eles não vão para a lixeira. Eles SOMEM!
'''

# Removendo para a lixeira:
from send2trash import send2trash

os.remove('cesta.txt')  # Não vai para a lixeira

send2trash('cesta2.txt')  # Vai para a lixeira. Pode ser restaurado
# OBS: Se o arquivo não existir, teremos OSError.

# Trabalhando com arquivos e diretórios temporários:

# Criando um diretório temporário:
'''
Estamos crianco um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. 
No final , usamos um input() só para mantermos os arquivos temporários 'vivos' dentro do bloco with. 
'''
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei diretório temporário em{tmp}')
    with open(os.path.join(tmp, 'asquivo_temporario.txt'), 'w', encoding='UTF-8') as arquivo:
        arquivo.write('Geek University\n')
    input()
'''
OBS: Possivelmente o codigo acima não irá funcionar se você estiver utilizando o Windows. Por conta desse sistema 
trabalhar de forma diferente com arquivos temporários.
'''

# Criando um arquivo temporário:
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')    # 'b' significa que o arquivo esta sendo escrito em binário.
    tmp.seek(0)
    print(tmp.read())

'''
Em arquivos temporários só conseguimos escrever em bits. por isso utilizamos 'b'.
'''
# Forma 2 - Sem o bloco with:
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek Universitu\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Forma 3:
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek Universitu\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()


