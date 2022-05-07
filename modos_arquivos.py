"""
MODOS DE ABERTURA ARQUIVO

r -> Abre para leitura (Padrao)
w -> Abre para escrita. (Sobreescreve caso o arquivo ja exista)
x -> Abre para escrita somente se o arquivo nao existir.Caso o arquivo exista, gera FileExistError.
a -> Abre para escrita, adicionando o conteudo no final do arquivo caso exista.
+ -> Abre para o modo de atualizacao, leitura e escrita. Temos o controle do cursor utilizando-o com 'r' ou 'w'.

https://docs.python.org/3/library/functions.html#open
"""

# EXEMPLO - Modo escrita 'x':

try:
    with open('university.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Texte de conteudo\n')
except FileExistsError:
  print('Arquivo ja existe')


# EXEMPLO - Modo escrita 'a' (append):
# OBS.: Com o modo 'a', nao controlamos o cursor.

with open('frutas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
      fruta = input('informe uma fruta ou digite sair: ')
      if fruta != 'sair':
        arquivo.write(fruta)
        arquivo.write('\n')
      else:
        break


# EXEMPLO - Modo escrita '+':

with open('texto.txt', 'r+', encoding='UTF-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('Nova linha\n')
    arquivo.write('Outra linha\n')
    arquivo.write('Mais uma linha.\n')