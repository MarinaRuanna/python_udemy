"""
POO - MÉTODOS MÁGICOS

Métodos Mágicos são todos os métodos que utilizam Dunder.

Dunder - > Dumble Underscore

EXEMPLO: - dunder init  -> __init__ -> Método construtor
         - dunder reper -> __repr__ -> Representação do objeto
         - dunder str   -> __str__  -> Reescreve a representação do objeto, tem preferencia em relação ao __repr__
         - dunder len   -> __len__
         - dunder del   -> __del__
         - dunder add   -> __add__

"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):          # Método __repr__ sobrescreve a representação do objeto.
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        return f'Um objeto do tipo Livro foi deletado da memória.'

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += '' + str(self)
            return msg
        return 'não foi possivel mutiplicar'


livro1 = Livro('Python rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek Rniversity', 350)

print(livro1)
print(repr(livro1))
print(len(livro1))


print(livro2)
print(repr(livro2))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)


