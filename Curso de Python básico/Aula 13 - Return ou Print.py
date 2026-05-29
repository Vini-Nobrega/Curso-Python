def apresentar(nome):
    print(f'Olá, {nome}. Tudo certo?')

apresentar('Vini')


def apresentar_2(nome):
    return(f'Olá, {nome}. Tudo certo?')

print(apresentar_2('Nóbrega'))


# O Return serve para a função TER um valor!!
# O Print, só printa algo no terminal, não guarda nenhum valor!
# Então, se eu der print no apresental vai retornar None, porque ele só printou, não armazenou o valor da print em lugar nenhum!
# Já o return, ele guarda a info. Então, o apresentar_2 sempre vai ter guardado o que é passado, não vai apenas printar!
