#3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
#tiver entre 16 e 18 anos
#já tiver jogado pelo menos 3 jogos
#Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em negrito e as impressões de seu código em itálico (apenas para facilitar sua visualização).
#Digite sua idade: 17
#Já jogou pelo menos 3 jogos de tabuleiro? True
#Quantos jogos já venceu? 2
#Apto para ingressar no clube de jogos de tabuleiro: True

idade=int(input("Digite sua idade:")) #tiver entre 16 e 18 anos=true
qtde_jogos=int(input("Quantos jogos de tabuleiro já jogou? :")) #pelo menos 3 jogos de tabuleiro=True
qtde_vitorias=int(input("Quantos jogos já venceu?:")) #já ter vencido pelo menos 1 jogo=true
apto=((idade >= 16 and idade <= 18) and (qtde_jogos >=3) and (qtde_vitorias >= 1))
print(f"Apto para ingressar no clube de jogos de tabuleiro:{apto}")