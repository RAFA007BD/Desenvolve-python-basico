qtde_registros=int(input("Digite a quantidade de registros: ")) #Variável de entrada
cont=0 #Laço
soma_s, soma_r, soma_c = 0,0,0
qtde_cobaias=0

while cont < qtde_registros:
      qtde_cobaias = int(input("Qtde Cobaias: "))
      tipo= input("Tipo da Cobaia ( S, R ou C): ")
              
      cont += 1
      

if tipo == 'S':
    soma_s = soma_s + qtde_cobaias
elif tipo == 'R':
    soma_r = soma_r + qtde_cobaias
elif tipo == 'C':
    soma_c = soma_c + qtde_cobaias
       
      
print(f"Total de Cobaias:{soma_s+soma_r+soma_c}")
print(f"Total de Coelhos:{soma_c}")
print(f"Total de Ratos:{soma_r}")
print(f"Total de Sapos:{soma_s}")
print(f"Percentual de Sapos: {soma_s / qtde_cobaias}%") 
print(f"Percentual de Ratos: {soma_r / qtde_cobaias}%") 
print(f"Percentual de Coelhos: {soma_s / qtde_cobaias}%") 

   
print("Fim")