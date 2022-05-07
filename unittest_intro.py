"""
UNITTEST

Unittest -> Testes unitários

https://docs.python.org/3/library/unittest.html

O que são testes unitários?
Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais -> Funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os assertions presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de testes para a sua unidade

# Conhecendo as assertions:

Método                           Checa que:
assertEqual(a, b)                a == b
assertNotEqual(a, b)             a != b
assertTrue(x)                    x é verdadeiro
assertFalse(x)                   x é falso
assertIs(a, b)                   a é b
assertNotIs(a,b)                 a não é b
assertIsNone(x)                  x é None
assertIsNotNone(x)               x não é None
assertIn(a, b)                   a está em b
assertNotIn(a, b)                a não está em b
assertIsInstance(a, b)           a é instância de b
assertNotIsInstance(a, b)        a não é instância de b


Por convenção, todos os testes em um test case, devem ter seu nome iniciado com test__

# Para executar os testes com unittest:  python nome_do_modulo.py

# Para executar os testes vom unittest no modo verbose: python nome_do_modulo -v

# Docstrings nos testes:

Pdem,os adicionar, e é recomendado, docstrings nos nossos testes.

"""

# Prática - Utilizando a abordagem TDD:

'''
vide módulos atividades.py e teste.py
'''
