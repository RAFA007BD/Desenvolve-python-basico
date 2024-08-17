import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

contador_lista1 = Counter(lista1)
contador_lista2 = Counter(lista2)

interseccao = sorted(set(lista1) & set(lista2))

print("Lista 1:")
print(lista1)
print("\nLista 2:")
print(lista2)

print("\nInterseccao:")
print(interseccao)

print("\nContagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={contador_lista1[valor]}, lista2={contador_lista2[valor]})")
