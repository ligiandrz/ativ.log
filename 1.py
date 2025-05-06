# Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
valorA = float(input("insira o valor de A: "))
valorB = float(input("insira o valor de B: "))
valorC = float(input("insira o valor de C: "))
soma = valorA + valorB 
print (f"o valor da soma de A e B é:{soma}")
if soma > valorC:
  print (" a soma de A e B é maior que C")
else:
  print (" a soma de A e B é menor que C")
