class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}.')

    def verificar_status(self):
        print(f'Status - Ativo' if self.status else 'Status - Inativo')


class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano

    def apresentar(self):
        super().apresentar()
        print('Eu sou um aluno da escola.')

    def verificar_status(self):
        super().verificar_status()


class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia

    def apresentar(self):
        super().apresentar()
        print('Eu sou um Professor da escola.')

    def verificar_status(self):
        super().verificar_status()


class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

    def apresentar(self):
        super().apresentar()
        print('Eu sou assistente da escola.')

    def verificar_status(self):
        super().verificar_status()


aluno_1 = Aluno(nome='Eduardo', idade=10, status=True, ano=4)
aluno_1.apresentar()
aluno_1.verificar_status()

print('\n')

professor_1 = Professor(nome='Andre', idade=50, status=False, materia='Matemática')
professor_1.apresentar()
professor_1.verificar_status()

print('\n')

assistente_1 = Assistente(nome='Vini', idade=20, status=True, bloco='Bloco A')
assistente_1.apresentar()
assistente_1.verificar_status()