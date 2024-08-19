import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        letras_do_meio = list(palavra[1:-1])
        random.shuffle(letras_do_meio)
        return palavra[0] + ''.join(letras_do_meio) + palavra[-1]

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
frase = input("Digite uma frase: ")
frase_embaralhada = embaralhar_palavras(frase)
print(frase_embaralhada)
