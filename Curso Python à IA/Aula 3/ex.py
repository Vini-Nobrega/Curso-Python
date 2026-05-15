quantidade = int(input("Quantas porções o produto tem: "))

uso_diario = int(input('Quantas porções você usa por dia: '))

v_duracao = quantidade / uso_diario

print(f'O produto vai durar por {v_duracao:.0f} dias . ') # :.0f -> Fala quantas casas decimais eu quero que mostre.