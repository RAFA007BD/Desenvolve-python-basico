def contar_espacos(frase):
    contagem = frase.count(' ')
    return contagem

def main():
    frase = input("Digite uma frase: ")
    
    numero_de_espacos = contar_espacos(frase)
    
    print(f"A frase contém {numero_de_espacos} espaço(s) em branco(s).")

if __name__ == "__main__":
    main()
