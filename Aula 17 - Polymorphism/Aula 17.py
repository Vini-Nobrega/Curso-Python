# # Polymorphism
# class Personagens():
#     def falar(self):
#         print(f'Eu sou um personagem')


# class Guerreiro(Personagens):
#     def falar(self):
#         print(f'Eu sou um guerreiro forte e destemido!')


# class Mago(Personagens):
#     def falar(self):
#         print(f'Eu sou um mago sábio e poderoso!')


# class Arqueiro(Personagens):
#     def falar(self):
#         print(f'Eu sou um arqueiro rápido e furtivo!')


# personagens_lista = [
#     Guerreiro(),
#     Mago(),
#     Arqueiro()
# ]

# for p in personagens_lista:
#     p.falar()

class Cachorro():
    def emitir_som (self):
        print('Au au au')

class Gato():
    def emitir_som(self):
        print('Miau Miau')

animais = [
    Cachorro(),
    Gato()
]

for a in animais:
    a.emitir_som()