"""
UNITTEST - ANTES E APÓS HOOKS

___
hooks -> São os testes em si,. Ou seja, a execução dos testes.
---

setup() -> Executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados:

tearDown() -> Executado ao final de cada método de teste. É útil para excluir dados
ou fechar conexões com banco de dados.
"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # Setup() vai rodar antes do teste
        # tearDown() vai rodar depois do teste
        pass

    def test_segundo(self):
        # Setup() vai rodar antes do teste
        # tearDown() vai rodar depois do teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
