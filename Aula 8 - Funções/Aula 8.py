#Funções

# def recepcao(nome, idade):
#     print(f'Olá, {nome}. Você tem {idade} anos de idade.')

# recepcao('Vini', 20)

# recepcao('Vini Nóbrega', 19)

# def somar(x,y):
#     return x + y

# total = somar(50,50)

# print(f'O valor total da minha soma é de {total}')

def calcular_desconto(valor_produto, porcentagem):
    return valor_produto - (valor_produto * porcentagem / 100)

valor_final = calcular_desconto(340,33)

print(f'O valor final, com desconto aplicado é de R${valor_final:.2f}')