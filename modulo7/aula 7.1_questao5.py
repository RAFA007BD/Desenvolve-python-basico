def contar_vogais_e_indices(frase):
    vogais = "aeiou"
    
    contagem_vogais = {vogal: {"contagem": 0, "indices": []} for vogal in vogais}
    
   
    if letra in vogais:
            contagem_vogais[letra]["contagem"] += 1
            contagem_vogais[letra]["indices"].append(i)
    
    return contagem_vogais

def main():
    frase = input("Digite uma frase: ")
    
    resultado = contar_vogais_e_indices(frase)
    
    for vogal, dados in resultado.items():
        print(f"Vogal '{vogal}' aparece {dados['contagem']} vez(es) nos índices {dados['indices']}.")

if __name__ == "__main__":
    main()
