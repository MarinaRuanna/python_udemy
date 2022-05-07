"""
POO - OBJETOS

Objetos -> São instâncias das classes. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos pode criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe
como variáveis do tipo definido na classe.
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome= nome
        self.__cpf = cpf
    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador +1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]




# Instâncias/Objetos:
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lampada está ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Marina', 'Ruanna', 'marina_ruana@hotmail.com', '123456')

cliente = Cliente('Marina', '102.648.884-08')

cc = ContaCorrente(5000, 10000)

cc.mostra_cliente()
cc._ContaCorrente__cliente.__diz()