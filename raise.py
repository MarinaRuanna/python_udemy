"""
RAISE - Levantando os próprios erros com raise

raise -> Lança exceções.

OBS: O raise não é uma função, é uma palavra reservada assim como def, None ou return.
Para simplificar, pense no raise como sendo útil para que possamos criar nossas proprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')

OBS: O raise assim como o return finaliza a função, ou seja, nada após o raise é executado.
"""


# EXEMPLO:
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'Azul')

# colore('Geek', 45)     # TypeError: cor precisa ser uma string

# Refatorando:

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'verde')

# colore('Geek', 'preto') # ValueError: cor precisa ser uma entre ('verde', 'amarelo', 'azul', 'branco')


