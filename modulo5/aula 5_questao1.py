num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))

diferenca = abs(num1 - num2)

diferenca_arredondada = round(diferenca, 2)

print(f"A diferença absoluta entre {num1} e {num2} é: {diferenca_arredondada}")
