"""
PORQUE TESTAR NOSSO CÓDIGO?

Testes Automatizados!

      aplicação web
_________________________
|                       |
| frontend e backend    |
-------------------------
|  testes automatizados |
-------------------------

Porque testar nossos códigos?
    - Reduzir bugs (problemas) no código;
    - Teste garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração que custumamos fazer não tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então escreve o código mínimo suficiente para fazer o teste passar (ou sej, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;
Estes estágio de desenvolvimento do TDD, são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)




