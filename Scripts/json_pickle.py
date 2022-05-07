"""
JSON E PICKLE

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube...)
e terceiros (nós desenvolvedores).
"""

import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)