def obter_lista(nome_lista):
 
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista

def intercalar_listas(lista1, lista2):
   
    lista_combinada = []
    tamanho_minimo = min(len(lista1), len(lista2))
    
    
    for i in range(tamanho_minimo):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])
    
    
    lista_combinada.extend(lista1[tamanho_minimo:])
    lista_combinada.extend(lista2[tamanho_minimo:])
