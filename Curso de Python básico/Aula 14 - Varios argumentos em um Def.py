def numeros(*numeros):
    
    resultado = 0

    for n in numeros:
        resultado += n

    return resultado


x = numeros(1, 2, 3, 4, 5, 6, 7)



y = numeros(1,2,3)

if x > 0:
    print(f'Ok {x}')
else:
    print('Falha')

if y < 7:
    print(f'Menor que 7: {y}')