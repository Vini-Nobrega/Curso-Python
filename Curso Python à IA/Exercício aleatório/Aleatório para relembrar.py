class biblioteca:
    def __init__(self, nome_livro, genero):
        self.nome_livro = nome_livro
        self.genero = genero

class livros:
    def __init__(self):
        self.livros_lista = []

    def adicionar_livros(self, livros):

        self.livros_lista.append(livros)

    def percorrer_livros(self):
        for l in self.livros_lista:
            print(f'O Livro selecionado foi o: {l.nome_livro}, do gênero de {l.genero}')
        

livro_1 = biblioteca('Harry Potter', 'Aventura')

livro_adicionar = livros()

livro_adicionar.adicionar_livros(livro_1)
livro_adicionar.percorrer_livros()