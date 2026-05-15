# class Computador:
#     def __init__(self, modelo, cpu_memoria,cpu_nome,gpu_nome,gpu_memoria):
#         self.modelo = modelo
#         self.gpu = self.GPU(gpu_nome , gpu_memoria)
#         self.cpu = self.CPU(cpu_nome, cpu_memoria)

#     def config_pc(self):
        
#         print(f'PC: {self.modelo}')
        
#         self.gpu.mostrar_GPU()
#         self.cpu.mostrar_CPU()
        
    
#     class CPU:
#         def __init__(self, nome, memoria_gb):
            
#             self.memoria_gb = memoria_gb
#             self.nome = nome

#         def mostrar_CPU(self):
#             print(f'{self.nome} - {self.memoria_gb}')

#     class GPU:
#         def __init__(self,clock, nome_GPU):
            
#             self.clock = clock
#             self.nome_GPU = nome_GPU

#         def mostrar_GPU(self):
#             print(f'{self.clock} - {self.nome_GPU}')

# PC_1 = Computador('XP Serie S 2026',18,'CPU NOME', 'GPU NOME', 10)

# PC_1.config_pc()


class Biblioteca():
    def __init__(self, livro, genero):
        self.livro = livro
        self.genero = genero


class Livro():
    
    def __init__(self):

        self.livros = []

    def adicionar_livro(self, livro_add):
        self.livros.append(livro_add)

    def mostrar_livros(self):
        for l in self.livros:
            print(f'{l.livro} - {l.genero}')

livro_1 = Biblioteca('Teste 1', 'Ação')
livro_2 = Biblioteca('Teste 2', 'Romance')

Livros = Livro()

Livros.adicionar_livro(livro_1)
Livros.adicionar_livro(livro_2)
Livros.mostrar_livros()