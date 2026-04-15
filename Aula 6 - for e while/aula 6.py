# estão no caderno as anotações!
#
# for v_repetir_1_ate_5 in range(1,6): ---> Repete do 1 até o 5.
# print (v_repetir_1_ate_5)
#
# for v_5_ate_o_1 in range(5,0,-1): ---> Repete do 5 até o 1.
#     print (v_5_ate_o_1)


# Percorre do 1 até o 5!! Se não tivesse o i + 1, ia rodar infinitamente!

# i = 0

# while i < 5:
#     print(i)
#     i = i + 1

# senha = ''

# while senha != 'Senha123':
    
#     senha = input('Digite a senha correta')
# print('Acesso liberado')


# for v_for in range(11):
#     print (v_for)
    
    
# v_while = 0

# while v_while < 10:
#     v_while = v_while + 1
#     print(v_while)
    
    

# for v_pares in range(0,51,2): #Pares
#     print(v_pares)


# num = int(input("Digite um número: ")) #tabuada

# for v_range in range(0,11):
#     v_soma = num * v_range
#     print(f'{num}x{v_range}= {v_soma}')
#
num = int(input('Digite um número: '))
num_subtrai = num

for v_num in range(num,0,-1):
    while num_subtrai != 2:
        num_subtrai = num_subtrai - 1
        v_num = v_num * num_subtrai
        print(v_num)