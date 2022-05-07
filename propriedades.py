"""
POO - PROPRIEDADES (Properties)

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atributos. Esse métodos são
conhecidos por getters ou setters, onde os getters retornam o valor do atributo e os setters
alteram o valor do mesmo.

# EXEMPLO:

    '''
    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    '''
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite =  novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferencia paga pro quem realizou a transferencia

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor




conta1 = Conta('Marina', 150, 1500)
conta2 = Conta('Ruanna', 300, 2000)

print(conta1.extrato())
print(conta2.extrato())


soma = conta1.saldo + conta2.saldo

print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 789456
print(conta1.__dict__)

print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)
