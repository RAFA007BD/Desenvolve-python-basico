#Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. 
#Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir. O terreno possui 250m2 e custa R$512,490.50

#Entradas
comprimento=float(input("Digite o comprimento do terreno:"))
largura=float(input("Digite a largura do terreno:"))
preco_m2=float(input("Digite o valor do M²:"))

#fórmulas
area_m2=(comprimento*largura)
valor_final=(preco_m2*area_m2)

#Saidas
print(f"O terreno possui {area_m2}M² e custa R${valor_final:,.2f}")

