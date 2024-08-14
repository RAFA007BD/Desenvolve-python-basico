qtde_respondentes=int(input("Digite a quantidade de respondentes: ")) #Variável de entrada

soma=0 #Resultado 
cont=0 #Laço

while cont < qtde_respondentes:
      idade = int(input("idade: "))
      soma += idade    
      
      cont += 1

      media = soma / qtde_respondentes
      
print(f"A média das idades dos respondentes é:{media:.0f}")
   
print("Fim")
