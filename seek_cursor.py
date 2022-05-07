"""
SEEK E CURSOR

seek() -> Utilizada pra movimentar o cursor pelo arquivo.
Ela recebe um parâmetro que indica onde queremos colocar o cursor.

"""
'''
OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do seu computador 
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa 
conexão, para isso utilizamos a função close().

Passos para se trabalhar com o arquivo:

1 - Abrir o arquivo;
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo
'''

# 1 - Abrir o arquivo:
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo:
print(arquivo.read(50))  # Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo

# 3 - Fechar o arquivo:
arquivo.close()


'''
arquivo = open('texto.txt')

print(arquivo)

print(arquivo.read())

# Movimentando o cursor pelo arquivo usando a função seek():

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(20)


print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha

ret = arquivo.readline()

print(ret)

print(ret.split(' '))

# readlines() ->

linhas = arquivo.readlines()

print(linhas)

print(len(linhas))

# closed() -> Verifica se o arquivo está aberto ou fechado.

print(arquivo.closed)
'''

'''
OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError.
'''
