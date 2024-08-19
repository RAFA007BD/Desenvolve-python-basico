import re

def analisar_arquivo():
    nome_arquivo = r"python\\estomago.txt"
    
    try:
        # Abre o arquivo e lê todas as linhas
        with open(nome_arquivo, encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        # Imprimi as primeiras 25 linhas
        print("As primeiras 25 linhas do arquivo são:\n")
        for i in range(min(25, len(linhas))):
            print(linhas[i], end='')

        total_linhas = len(linhas)
        print(f"\n\nNúmero total de linhas no arquivo: {total_linhas}")

        # Encontra a linha com o maior número de caracteres
        linha_maior = max(linhas, key=len)
        print("\nA linha com o maior número de caracteres é:\n")
        print(linha_maior)

        # Conta o número de menções a Nonato e Íria
        mencoes_nonato = sum(1 for linha in linhas if re.search(r'\bnonato\b', linha, re.IGNORECASE))
        mencoes_iria = sum(1 for linha in linhas if re.search(r'\bíria\b', linha, re.IGNORECASE))

        print(f"\nNúmero de menções ao nome 'Nonato': {mencoes_nonato}")
        print(f"Número de menções ao nome 'Íria': {mencoes_iria}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    analisar_arquivo()
