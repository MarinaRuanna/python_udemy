"""
POO - HERANÇA (Inheritance)

A ideia de herança é a de reaproveitar código. Também estender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nos estendemos outra classe que passa a herdar atributos e métodos
da classe herdada.

# EXEMPLO:

Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario:
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade genérica suficiente para encapsular os atributos
e métodos comuns a outras entidades?

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a cçasse herdade é conhecida por:
      [Pessoa]
    - super classe
    - classe mãe
    - classe pai
    - classe base
    - classe genérica

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - sub classe
    - classe filha
    - classe específica

Sobrescrita de Método -> Ocorre quanbdo reescrevemos/reimplementamos um método presente na super classe em classes filhas.
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'



class Cliente(Pessoa):

    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)            # Forma não comun de acessar dados da super classe
        self.__renda = renda



class Funcionario(Pessoa):

    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)          # Forma não comun de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} nome: {self._Pessoa__nome}'


class Piguin:

    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

        
# Sobrescrita de Métodos (Overriding):
'''
Sobrescrita de Método -> Ocorre quanbdo reescrevemos/reimplementamos um método presente na super classe em classes filhas.
'''
cliente1 = Cliente('Marina', 'Ruanna', '102.642.884-08', 5000)
funcionario1 = Funcionario('João', 'Silva', '333.444.555-66', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
