import random

def adivinha_numero():
    
    numero_secreto = random.randint(1, 10) #geração de numero aleatorio
    
    
    acertei = False #variavel
    
    
    while not acertei: #execução
            
            palpite = int(input("Adivinhe o número entre 1 e 10: "))
            
            if palpite < 1 or palpite > 10:
                print("Por favor, escolha um número entre 1 e 10.")
                continue
            
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print("Parabéns! Você acertou o número!")
                acertei = True
        
       
# Chama a função para iniciar o jogo
adivinha_numero()
