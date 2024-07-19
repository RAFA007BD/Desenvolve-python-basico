#Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. 
#A mensagem deve estar formatada da seguinte maneira:
#86 graus Fahrenheit são 30 graus Celsius.

#Entrada de dados
graus_f=float(input("Digite a temperatura Fahrenheit:"))
graus_c=float(input("Digite a temperatura Celsius:"))

#Fórmulas
graus_c=(graus_f-32)*(5/9)

#Saida
print(graus_f, f"graus Fahrenheit são {graus_c:.2f} graus celsius.")