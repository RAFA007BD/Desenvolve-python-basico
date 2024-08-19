from collections import Counter

def encontrar_anagramas(s, palavra_objetivo):
    
    def sao_anagramas(str1, str2):
        return Counter(str1) == Counter(str2)
    
    anagramas = []
    comprimento_palavra = len(palavra_objetivo)
    
    for i in range(len(s) - comprimento_palavra + 1):
        substring = s[i:i + comprimento_palavra]
        if sao_anagramas(substring, palavra_objetivo):
            anagramas.append(substring)
    
    return anagramas

def main():
     
    s = input("Digite uma frase: ")
    palavra_objetivo = input("Digite qual palavra quer ver o anagrama: ")
   
    resultado = encontrar_anagramas(s, palavra_objetivo)
    
   
    if resultado:
        print("Anagramas encontrados:", resultado)
    else:
        print("Nenhum anagrama encontrado.")


if __name__ == "__main__":
    main()
