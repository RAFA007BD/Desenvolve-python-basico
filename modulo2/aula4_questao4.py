#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 
#Entrada: 576
# Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

#Entrada de dados
valor=int(input("Digite um valor:"))

#Processamento

notas_100=(valor//100) #Divisão com resto inteiro
valor=(valor%100) #Resto da divisão anterior
notas_50=(valor//50)
valor=(valor%50)
notas_20=(valor//20)
valor=(valor%20)
notas_10=(valor//10)
valor=(valor%10)
notas_5=(valor//5)
valor=(valor%5)
notas_2=(valor//2)
valor=(valor%2)
notas_1=(valor//1)
valor=(valor%1)

#Saida
print(notas_100,"nota(s) de R$100,00")
print(notas_50,"nota(s) de R$50,00")
print(notas_20,"nota(s) de R$20,00")
print(notas_10,"nota(s) de R$10,00")
print(notas_5,"nota(s) de R$5,00")
print(notas_2,"nota(s) de R$2,00")
print(notas_1,"nota(s) de R$1,00")