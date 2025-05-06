#Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.
numero = int(input("digite um número:"))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
