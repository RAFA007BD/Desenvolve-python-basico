#1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar.
# Lembre-se do operador do python % que retorna o resto de uma divisão.

#Entrada de dados
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))

#processamento
n3=(n1+n2)
#Condicional - Se resto da soma for igual a 0 o numero é par. Se não ele é ímpar.
if n3%2 == 0:
    print("Este número é par")
else:
    print("Este número é ímpar") 