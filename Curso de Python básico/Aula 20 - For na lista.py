cor_selecionada = input('Digite uma cor: ')

cores = ['azul', 'vermelho', 'preto', 'branco']

if cor_selecionada.lower() in cores:
    print(f'Temos a cor {cor_selecionada.lower()}')

else:
    print(f'Não temos a cor {cor_selecionada.lower()}')