# v_valida = True

# for v_loop in range(3):

#     if v_valida:
#         print('Compra aprovada')
        
#     else:
#         print('Compra reprovada')



# exemplo real que funciona

tentativas = [False, False, True]

for resultado in tentativas:
    print (resultado)
    if resultado:
        print(f'Compra aprovada')
        break

else:
    print('Compra reprovada')