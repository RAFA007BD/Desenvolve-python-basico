qtde_notas=int(input("Digite a quantidade de notas a serem analisadas: ")) #Variável de entrada

soma=0 #Resultado 
cont=0 #Laço

while cont < qtde_notas:
      nota = int(input("Nota: "))
      soma += nota    
      
      cont += 1

      media = soma / qtde_notas

   
if media >= 60:
    print("Aprovado")
elif media >= 40:
    print("Recuperação")
else:
    print("Reprovado")


print("Fim")
