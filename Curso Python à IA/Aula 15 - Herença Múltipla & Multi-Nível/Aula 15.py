class animal:
    def __init__(self, nome):
        self.nome = nome

class Predador(animal):
    def predar(self):
        print(f'O {self.nome} está caçando')

class Presa(animal):
    def fugir(self):
        print(f'O {self.nome} está fugindo do predador')

class animal_predador(Predador):
    pass

class animal_presa(Presa):
    pass

class animal_presa_e_predador(Predador,Presa):
    pass

animal_1 = animal_predador('Lobo')
animal_1.predar()
print('\n')
animal_2 = animal_presa('Coelho')
animal_2.fugir()
print('\n')
animal_3 = animal_presa_e_predador('Coiote')
animal_3.fugir()