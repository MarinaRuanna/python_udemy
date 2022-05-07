"""
ESCREVENDO UM ITERADOR CUSTOMIZADO

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration



'''
OBS: Para criar o nosso iterador customizado, precisamos utilizar o __next__ e o __iter__
OBS: __init__ Função especial chamada de contrutor, responsável por criar os objetos a partir da classe. 
'''

con = Contador(1, 6)

print(con)
print(con.maior)
print(con.menor)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for n in Contador(1, 61):      # Reproduzindo o range. Iterador customizado.
    print(n)


for n in range(1, 61):
    print(n)







