class banco:
    def __init__(self, valor_saque, valor_disponivel):

        self.valor_saque = valor_saque
        self.valor_disponivel = valor_disponivel

    def valor_de_saque(self):
        
        if self.valor_saque > self.valor_disponivel:
            print('\nSaldo insuficiente')
        
        else:
            novo_saldo = self.valor_disponivel - self.valor_saque

            print(f'\nSaque feito, seu novo saldo é de R${novo_saldo}')