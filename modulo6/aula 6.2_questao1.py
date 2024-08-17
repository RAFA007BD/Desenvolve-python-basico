import random

valores = [random.randint(-100, 100) for _ in range(20)]

valores_ordenados = sorted(valores)

indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

print("Lista ordenada (sem modificar a lista original):")
print(valores_ordenados)
print("\nLista original:")
print(valores)
print("\nÍndice do maior valor da lista original:")
print(indice_maior)
print("\nÍndice do menor valor da lista original:")
print(indice_menor)
