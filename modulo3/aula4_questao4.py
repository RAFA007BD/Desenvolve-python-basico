#4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
# screva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

#Entrada
distancia=float(input("Digite a distância (Em Km):"))
peso=float(input("Digite o peso do pacote (Em Kg):"))

#processamento
#a = distancia <=100 
#b = distancia >=101 and distancia <=300
#c = distancia >300


if peso >10:
   tx=10
else: tx=0     
if distancia <=100: 
   valor_kilo=1
elif distancia >=101 and distancia <=300:
   valor_kilo=1.5  
else: 
   valor_kilo=2

frete=((peso*valor_kilo)+tx)
print(f"O valor do frete é: R$",{frete})   

             

   
   
         