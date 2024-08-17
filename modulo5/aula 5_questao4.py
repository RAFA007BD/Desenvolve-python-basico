from datetime import datetime

def exibir_data_hora_atual():
    agora = datetime.now()
    formato = "%d/%m/%Y %H:%M"
    data_hora_formatada = agora.strftime(formato)
    print("Data e hora atuais:", data_hora_formatada)


exibir_data_hora_atual()
