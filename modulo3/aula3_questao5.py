#5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero=input("Qual o seu Gênero: (M ou F):")
idade=int(input("Qual a sua Idade:")) 
tempo=int(input("Qual o seu tempo de serviço:"))
aposenta=(genero == "F" and idade > 60 or tempo >= 30 or idade == 60 and tempo>=25) or (genero == "M" and idade > 65 or tempo >= 30 or idade == 60 and tempo>=25) 
print(f"Você já pode se aposentar: {aposenta}")