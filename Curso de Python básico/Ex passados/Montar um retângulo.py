formato = '@'
tamanho = 6
tamanho_2 = 6

for retangulo in range(tamanho):

    for retangulo_2 in range(tamanho_2):
        print (formato, end='')
    print() #---> Toda vez q terminar o segundo for, pula uma linha. Portanto, vai rodar 6 x o valor de 6, ai vai dar certo.