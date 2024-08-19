import os

def processar_frase():
    
    arquivo_entrada = "frase.txt"
    arquivo_saida = "palavras.txt"

    try:
        
        with open(arquivo_entrada, 'r') as arquivo:
            conteudo = arquivo.read()

        # Filtra apenas caracteres alfabéticos e espaços
        palavras = ''.join(caractere if caractere.isalpha() or caractere.isspace() else ' ' for caractere in conteudo)
        
        # Separa palavras por espaços e remove-as
        lista_palavras = palavras.split()

        # Escreve as palavras no arquivo de saída, uma por linha
        with open(arquivo_saida, 'w') as arquivo:
            for palavra in lista_palavras:
                arquivo.write(palavra + '\n')

        
        with open(arquivo_saida, 'r') as arquivo:
            conteudo_final = arquivo.read()

        print("Conteúdo do arquivo 'palavras.txt':")
        print(conteudo_final)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")

if __name__ == "__main__":
    processar_frase()
