import string

def verificar_palindromo(frase):
    # Remove espaços e pontuações e converte para minúsculas
    frase_limpa = ''.join(caractere for caractere in frase if caractere.isalnum()).lower()
    
    # Verifica se a frase limpa é igual ao contrario
    return frase_limpa == frase_limpa[::-1]

def main():
    while True:
        frase = input("Digite uma frase para verificar se é um palíndromo (ou 'Fim' para encerrar): ")
        
        if frase.lower() == "fim":
            print("Programa encerrado.")
            break
        
        if verificar_palindromo(frase):
            print("A frase é um palíndromo!")
        else:
            print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()
