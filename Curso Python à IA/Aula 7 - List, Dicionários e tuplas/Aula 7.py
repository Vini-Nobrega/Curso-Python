# frutas = ['Maçã','Banana','Pêra']
# #print(frutas[1]) --> Pegar um index em específico
# frutas.append('Manga') # Adiciona algo na lista
# frutas.append('Morango')
# #frutas.remove('Banana') --> Remover algo da lista
# print(len(frutas)) # Retorna o tamanho da lista em números. Por ex: 5 (itens)
# print(frutas)


#Percorrer todos os itens da lista:

#LISTA

# tarefas = []
# tarefas.append('Acordar')
# tarefas.append('Estudar')
# tarefas.append('Trabalhar')
# for tarefas_percorrer in tarefas:
#     print(f'Tarefas à fazer: {tarefas_percorrer}')


#TUPLAS

# Tarefas = ('Arroz','Feijão')
# #Tarefas.append('Macarrão') --> Não vai funcionar! É uma tupla!!
# # print(Tarefas[0]) --> Retornaria Arroz normal.


#Dicionário

# usuario = {
#     'nome': 'Vini',
#     'idade': 20,
#     'Departamento':'TI'
# }

# usuario['Nome'] = 'Vinicius Nóbrega'
# usuario['Cidade'] = 'São Paulo'

# print(usuario)


aluno = {
    'nome':input('Nome do aluno: '),
    'idade':input('Idade do aluno: '),
    'nota':float(input('Nota do aluno: '))
}

print(f'O aluno {aluno["nome"]}, de {aluno["idade"]} anos de idade, tirou nota {aluno["nota"]} este semestre')  