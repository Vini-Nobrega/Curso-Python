class casa:
    def __init__(self,cor,banheiros):
        self.cor = cor
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
    
    def quantidade_banheiros(self):
        print(f'A quantidade de banheiros que tem na casa é de {self.banheiros}')

casa_1 = casa('Azul',2)
casa_2 = casa('Roxo',5)

print('\nCasa 1: ')
casa_1.mostrar_cor()
casa_1.quantidade_banheiros()

print('\nCasa 2: ')
casa_2.mostrar_cor()
casa_2.quantidade_banheiros()