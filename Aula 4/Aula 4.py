# num1 = 10
# num2 = 20

# print(num1 == num2)
# print(num1 != num2)
# print(num1 > num2)
# print(num1 < num2)
# print(num1 <= num2)
# print(num1 >= num2)


#Verificar se pode dirigir

# carteira = True
# idade = int(input('Digite sua idade: '))
# verificador = idade >= 18 and carteira
# print(verificador)

usuario = input('Digite seu usuario: ') 
senha = input('Digite sua senha: ')

validar_login = usuario == 'Admin' and senha == '123admin'

print(f'Login permitido: {validar_login}')