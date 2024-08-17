
numeros = []
print("Digite pelo menos 4 números inteiros (digite 'fim' para encerrar):")

while True:
    entrada = input("Digite um número: ")
    
    if entrada.lower() == 'fim':
        if len(numeros) < 4:
            print("Insira pelo menos 4 números.")
        else:
            break
    else:
            numero = int(entrada)
            numeros.append(numero)
        
print("\nLista original:")
print(numeros)

print("\nOs 3 primeiros elementos:")
print(numeros[:3])

print("\nOs 2 últimos elementos:")
print(numeros[-2:])

print("\nLista invertida:")
print(numeros[::-1])

print("\nElementos de índice par:")
print(numeros[::2])

print("\nElementos de índice ímpar:")
print(numeros[1::2])
