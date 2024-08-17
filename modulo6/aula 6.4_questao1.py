pares_entre_20_e_50 = [num for num in range(20, 51) if num % 2 == 0]

quadrados = [x**2 for x in range(1, 10)]

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]

paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]

print("Números pares entre 20 e 50:")
print(pares_entre_20_e_50)

print("\nQuadrados dos valores de 1 a 9:")
print(quadrados)

print("\nNúmeros entre 1 e 100 divisíveis por 7:")
print(divisiveis_por_7)

print("\nParidade dos valores em range(0, 30, 3):")
print(paridade)
