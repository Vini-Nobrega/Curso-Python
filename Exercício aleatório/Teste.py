class carro:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligar = False
    
    def modelo_carro(self):
        print(f'A cor do seu carro é {self.modelo}')

    def cor_carro(self):
        print(f'A cor do seu carro é {self.cor}')

    def ano_do_carro(self):
        print(f'O ano do seu carro é {self.ano}')

    def ligar_carro(self):
        
        if self.ligar:
            print('Seu carro já está ligado')
        
        else:
            print('Seu carro foi ligado')