"""
LEITURA DE ARQUIVOS

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa abrir.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é
o nome do arquivo a ser ido. Essa função retona um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r'

mode r -> Modo de leitura. r -> read() -> ler


"""
# EXEMPLO:

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))


'''
Para ler um conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
'''

print(arquivo.read())

'''
O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, 
funciona como o cursor quando estamos escrevendo.

A função read() lê todo o conteudo do arquivo.
'''

arquivo.close()

print(arquivo.closed)
