class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'O animal é da espécie {self.especie}, chamado de {self.nome}.')


class Gato(Animal):
    def emitir_som(self):
        print('Miau')

    def acao(self):
        print(f'O gato {self.nome} pulou')


class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au')

    def acao(self):
        print(f'A cachorra {self.nome}, abanou o rabo')


class Elefante(Animal):
    def emitir_som(self):
        print('**Barulhos de Elefante**')

    def acao(self):
        print(f'O elefante {self.nome} levantou as orelhas')


gato_1 = Gato('Felix', 'Marrom', 'Siamese')
gato_1.apresentar()
gato_1.emitir_som()
gato_1.acao()

print('\n')

cachorro_1 = Cachorro('Laura', 'Branca', 'Chihuahua')
cachorro_1.apresentar()
cachorro_1.emitir_som()
cachorro_1.acao()

print('\n')

cachorro_2 = Cachorro('Bob', 'Branco', 'Shitzu')
cachorro_2.apresentar()

print('\n')

elefante_1 = Elefante('Dumbo', 'Cinza', 'Elefante Africano')
elefante_1.apresentar()
elefante_1.emitir_som()
elefante_1.acao()
