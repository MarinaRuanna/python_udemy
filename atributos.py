"""
ATRIBUTOS

Atributos representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos.

# Atributos de Instância: São atributos declarados dentro do método construtor

* Método construtor é um método especial utilizado para a cosntrução do objeto.

- Em Java, uma classe Lampada, incluindo seus atributos ficaria mais ou menos assim:

public class Lampada(){
    private int voltagem:
    private String cor:
    private Boolean ligada = false:

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem:
        this.cor = cor
    }
}

Em Python, por convenção ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado
dentro da propria classe onde está declarado, utiliza-sse __ duplo underscore no inicio de seu nome.

Isso é conhecido também como MangLing.
"""

# Atributos de Instância:


# Atributos Públicos e Atributos Privados:


# Classes com Atributo de Instância Público:
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# self é o objeto que está executando o método:


# Classes com Atributos de Instância Privados:

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

'''
OBS: Lmebre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos 
atributos sinalizados como privados fora da classe.
'''

# EXEMPLO:

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AttributeError

# print(user._Acesso__senha) # Temos acesso. Mas não deverámos fazer esse acesso. (Name MangLing)

user.mostra_senha()

user.mostra_email()

# O que significa Atributos de Intâncias:
'''
Significa que ao criarmos Instâncias/Objetos de um classe, todas as instâncias terão estes atributos.
'''

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '123456')

user1.mostra_email()

user2.mostra_email()

# Atributos de Classes:

'''
Atributos de Classe, são atributos que são declarados diretamente na classe, ou seja, fora do construtor. 
Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe, ou seja, 
ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, 
com os atributos de classe, todas as instâncias terão o mesmo valor para este atributo.
'''

# Refatorando a classe Produto:

class Produtos:

    # Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produtos.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produtos.imposto)
        Produtos.contador = self.id

p1 = Produtos('Playstation 4', 'Video-game', 2300)
p2 = Produtos('Xbox S', 'Video-game', 4500)

print(p1.imposto)
print(p2.imposto)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor) # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso ao atributo de classe.

print(Produtos.imposto) # Acesso correto de um atributo de classe.

print(p1.id)
print(p2.id)

'''
OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe em Python 
são chamados de atributos estáticos;
'''

# Atributos Dinâmicos:

# Um atributo de Instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.


p3 = Produtos('Playstation 4', 'Video-game', 2300)
p4 = Produtos('Xbox S', 'Video-game', 4500)

p3.peso = '5kg' # Note que na classe Produtos não existe o atributo peso.

print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

# print(f'Produto: {p4.nome}, Descrição: {p4.descricao}, Valor: {p4.valor}, Peso: {p4.peso}')

# Deletando atributos:

print(p3.__dict__)
print(p4.__dict__)

print(Produtos.__dict__)

del p3.peso

print(p3.__dict__)
print(p4.__dict__)