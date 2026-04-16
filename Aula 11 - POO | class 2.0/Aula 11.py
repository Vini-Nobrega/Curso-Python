# class carro:
#     def __init__(self,carro,placa,cor):
#         self.carro = carro
#         self.placa = placa
#         self.cor = cor

#     def modelo_carro(self):
#         print(f'O modelo do seu carro é {self.carro}')

#     def placa_do_carro(self):
#         print(f'A placa do seu carro é {self.placa}')

#     def cor_do_carro(self):
#         print(f'A cor do seu carro é {self.cor}')

# carro_1 = carro(input('Carro 1:'),input('Placa 1: '),input('Cor 2: '))

# carro_2 = carro(input('Carro 2: '),input('Placa 2: '),input('Cor 2: '))

# print('\nCarro 1:')

# carro_1.modelo_carro()
# carro_1.placa_do_carro()
# carro_1.cor_do_carro()

# print('\nCarro 2:')

# carro_2.modelo_carro()
# carro_2.placa_do_carro()
# carro_2.cor_do_carro()

class carro:
    def __init__(self, carro, ano):
        self.carro = carro
        self.ano = ano
        self.ligado = True
        self.seta = None

    def modelo_carro(self):
        print(f'O modelo do seu carro é {self.carro}.')
        print(f'O ano do carro é {self.ano}.')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro estava desligado')

    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Você não pode dar seta porque o carro está desligado.')
            return
        
        self.seta = direcao
        print(f'Seta para {self.seta}')
            


carro_1 = carro('Azul', '2021')

carro_1.modelo_carro
carro_1.ligar()
#carro_1.desligar()
carro_1.ligar_seta('Esquerda')