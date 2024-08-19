def formatar_numero(numero):
      
    if len(numero) == 8:
        numero = '9' + numero
    elif len(numero) == 9:
        if numero[0] != '9':
            return "Número inválido: O primeiro dígito deve ser 9."
    else:
        return "Número inválido: O número deve ter 8 ou 9 dígitos."
    
    numero_formatado = (f"{numero[:2]}-{numero[2:7]}-{numero[7:]}")
    
    return numero_formatado

def main():
    numero = input("Digite o número de celular: ")
    
    resultado = formatar_numero(numero)
    
    print("Número formatado:", resultado)

if __name__ == "__main__":
    main()
