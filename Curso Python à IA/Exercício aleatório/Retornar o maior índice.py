def longest_word(text):
    lista = text.split() #ta com o texto do print
    lista_maior = []
    for c in lista:
        lista_maior.append(len(c))
    
    maior_num = max(lista_maior)
    indice_maior_num = lista_maior.index(maior_num)
    return lista[indice_maior_num]
    
print(longest_word('Monty Python and the Holy Grail'))