class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos de idade.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)

        self.cargo = cargo

    def Trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}!')


class Cliente(Pessoa):
    def __init__(self, nome, idade,saldo):
        super().__init__(nome, idade)
        self.saldo = saldo
    
    def saldo_disponivel(self):
        print(f'O saldo disponível do Cliente {self.nome}, de {self.idade} anos de idade é de R$ {self.saldo}.')

    def comprar_produto(self, v_compra):
        
        if self.saldo >= v_compra:

            self.saldo -= v_compra

            print(f'Compra de R$ {v_compra} aprovada. Seu novo saldo é de R$ {self.saldo}.')

        else:
            print(f'Não é possível comprar, o valor do produto é de R$ {v_compra}. O saldo atual do {self.nome} é de R$ {self.saldo}')


f1 = Funcionario('Vini', 20, 'Estagiário')
f1.apresentar()
f1.Trabalhar()

print('\n')

c1 = Cliente('Kevin', 23, 500)
c1.apresentar()
c1.saldo_disponivel()
c1.comprar_produto(100)