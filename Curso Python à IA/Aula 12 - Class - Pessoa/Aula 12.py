class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promocao(self, novo_cargo):
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}')
        self.cargo = novo_cargo


    def atualizar_idade(self,nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando idade de {self.idade} para {nova_idade}')
        else:
            print(f'A idade não pode ser menor que a atual')

pessoa_1 = Pessoa('Vini do Exército',19,'Estagiário')
pessoa_2 = Pessoa('Vini pós Exército',20,'Estagiário Plus')

pessoa_1.informacoes()
print("\n") 
# pessoa_2.promocao('Desenvolvedor Jr') 
pessoa_2.informacoes()
pessoa_2.atualizar_idade(21)
