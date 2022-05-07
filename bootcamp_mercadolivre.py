"""
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos,
onde cada um seja menor ou igual a <maxDigit>, e a soma dos dígitos de cada número gerado seja 21.

EXEMPLO: maxDigit = 6: 3666, 4566, 5566...
"""


maxDigit = input('digite um numero de 1 a 9:')



def verificar_digito(inicio=1000, fim=10000, soma_digitos=21):
    lista_numeros =[]
    for numero in range(inicio, fim):
        digitos = [int(digito) for digito in str(numero)]
        if max(digitos) <= int(maxDigit) and sum(digitos) == soma_digitos:
                lista_numeros.append(numero)
                print(numero)
    if not lista_numeros:
            print('null')


verificar_digito()

