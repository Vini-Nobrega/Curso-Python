class Biblioteca():
    def __init__(self, nome_livro, genero_livro, qntd_paginas, disponibilidade):
        self.nome_livro = nome_livro
        self.genero_livro = genero_livro
        self.qntd_paginas = qntd_paginas
        self.disponibilidade = disponibilidade

class Livros(Biblioteca):
    def __init__(self):
        self.lista_livros = []
    
    def adicionar_livros(self,livro):
        self.lista_livros.append(livro)

    def mostrar_livros(self):
        for l in self.lista_livros:
            print(f'O livro {l.nome_livro}, do gênero {l.genero_livro}, tem {l.qntd_paginas}')
            print(f'Status: Disponível' if l.disponibilidade else 'Status: Indisponível')
            print('\n')
# Criar os livros

livro_biblioteca_1 = Biblioteca('O homem de Giz', 'Terror', 240, True)
livro_biblioteca_2 = Biblioteca('Harry Potter', 'Ação', 352, False)
livro_biblioteca_3 = Biblioteca('O pequeno príncipe', 'Aventura', 200, True)

# Criar lista com os livros

Lista_livros = Livros()

Lista_livros.adicionar_livros(livro_biblioteca_1)
Lista_livros.adicionar_livros(livro_biblioteca_2)
Lista_livros.adicionar_livros(livro_biblioteca_3)

# Mostar livros

Lista_livros.mostrar_livros()