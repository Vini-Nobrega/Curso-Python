class casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')

    def quantidade_de_quartos(self):
        print(f'A quantidade de quartos da casa é de {self.quartos}')

    def quantidade_banheiros(self):
        print(f'Tem {self.banheiros} banheiro(s) na casa.')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'A casa tem {self.quartos}')

    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')


casa_1 = casa('Azul', 4, 5)
casa_2 = casa('Preta', 2, 1)

print('\nCasa 1:')
casa_1.mostrar_cor()
casa_1.quantidade_de_quartos()
casa_1.quantidade_banheiros()
casa_1.adicionar_quarto()
casa_1.pintar_casa(input('Digite a nova cor da casa: '))

print('\nCasa 2:')
casa_2.mostrar_cor()
casa_2.quantidade_de_quartos()
casa_2.quantidade_banheiros()
casa_2.adicionar_quarto()
casa_2.pintar_casa(input('Digite a nova cor da casa: '))