"""
São todos os métodos que utilizam o __
__init__
Dunder > Double underscore
"""
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # em vez de mostrar o local o objeto na memoria ele retorna os valores
        return f'{self.titulo}, Escrito por: {self.autor}, {self.paginas}'

    def __str__(self):  # quando colocar o str ele ignora o repr
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'um objeto do tipo livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'



livro1 = Livro('Python rocks', 'Geek University', 400)
livro2 = Livro('Intelgência artificial', 'Geek University', 350)

print(str(livro1))
print(str(livro2))

print(livro1 + livro2)
print(livro2 * 3)


