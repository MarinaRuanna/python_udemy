import math

def circunferecia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

# print(circunferecia(8))

# print(circunferecia('Geek'))

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()}".center(50, '#')



def cabecalho2(
        texto, # type: str
        alinhamento=True # type: bool
): # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'
    
cabecalho2(texto='42', alinhamento=False)

nome = 'Geek University' # type: str


