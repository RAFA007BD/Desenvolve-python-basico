def formatar_data(data):
    
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    dia, mes, ano = data.split('/')
    
    # Converte o mês de string para número e ajusta para zero baseado em lista de meses
    mes = int(mes)
    
    # Obtem o nome do mês correspondente
    nome_mes = meses[mes - 1]
    
    # Formata a data com o nome do mês por extenso
    data_formatada = f"{dia} de {nome_mes} de {ano}"
    
    return data_formatada

def main():
    
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
    resultado = formatar_data(data)
    
    print(f"Você nasceu em {resultado}.")


if __name__ == "__main__":
    main()
