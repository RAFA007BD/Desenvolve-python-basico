frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

lista_vogais = sorted([caractere for caractere in frase if caractere in vogais])

lista_consoantes = [caractere for caractere in frase if caractere.isalpha() and caractere not in vogais]

print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
