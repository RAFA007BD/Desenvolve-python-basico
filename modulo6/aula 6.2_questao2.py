import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) 
             for _ in range(num_elementos)]

soma_elementos = sum(elementos)

media_elementos = soma_elementos / num_elementos

print("Lista de elementos:")
print(elementos)
print("\nSoma dos valores da lista:")
print(soma_elementos)
print("\nMédia dos valores da lista:")
print(media_elementos)
