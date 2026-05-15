Produtos = [
    {'Nome': 'Arroz', 'Preço': 25},
    {'Nome': 'Feijão', 'Preço': 38},
    {'Nome': 'Batata', 'Preço': 60},
    {'Nome': 'Macarrão', 'Preço': 10},
    {'Nome': 'Doce', 'Preço': 60}
]

while True:

    try:
        v_disponivel = int(input('Digite seu saldo: R$: '))
        break

    except ValueError:
        print('Por favor, digite apenas números.')

print()

print(f'R${v_disponivel} disponível')

print()

v_encontrou = False

for p in Produtos:

    if p['Preço'] < v_disponivel:

        print(f"Produtos disponíveis: {p}")
        v_encontrou = True

if v_encontrou:
    print()
    v_produto_desejado = input('Qual produto você deseja comprar: ')

else:
    print('Não há nenhum produto em estoque dentro do seu orçamento.\n')
    exit()

v_produto_confirmado = False

while v_produto_confirmado == False:

    for p_nome in Produtos:

        if v_produto_desejado == p_nome['Nome']:

            v_preco = p_nome['Preço']
            print()
            print('Produto confirmado!\n')

            v_produto_confirmado = True
            break

    if v_produto_confirmado == False:

        v_produto_desejado = input('Digite o produto certo: ')

print(f'Ok, até agora a sua compra é a seguinte:\nProduto: {v_produto_desejado}\nValor: R${v_preco}\nDeseja continuar com a compra?\n')

v_confirmar_compra = input(
    'Digita "Sim" para confirmar OU Digite "Não" para recusar: ')

v_confirmar_compra = v_confirmar_compra.lower()

while v_confirmar_compra != "sim" and v_confirmar_compra != "não":

    v_confirmar_compra = input('Por favor, digite apenas "Sim" ou "Não": ')

if v_confirmar_compra == "sim":
    print('Compra confirmada.\nRealizando compra!\n')

    v_disponivel -= v_preco

    print(f'Seu novo saldo é de R${v_disponivel}.\nAté breve!\n')

else:
    print('Pedido Cancelado com sucesso.\nAté breve!\n')