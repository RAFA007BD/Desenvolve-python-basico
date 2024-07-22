#2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). 
# Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

juliana=int(input("Digite a idade da Juliana:"))
cris=int(input("Digite a idade da Cris:"))
maiorid=int(input("Digite a idade da pessoa mais velha do grupo:"))
print((juliana and cris > 17)or (maiorid > 17))
