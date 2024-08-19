def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    
    frase_modificada = ''.join('*' if letra in vogais else letra for letra in frase)
    
    return frase_modificada

def main():
    
    frase = input("Digite uma frase: ")
   
    resultado = substituir_vogais(frase)
    
    print("Frase modificada:", resultado)


if __name__ == "__main__":
    main()
