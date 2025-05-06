#Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se
#ambos são VERDADEIRO ou FALSO. Sendo o numero 1 Verdadeiro e 0 Falso.
valor1 =int(input("digite o primeiro valor(1 para verdadeiro, 0 para falso):"))
valor2 =int(input("digite o segundo valor(1 para verdadeiro, 0 para falso):"))
if valor1 == 1 and valor2 == 1:
        print("ambos são verdadeiros")
elif valor1 == 0 and valor2 == 0:
        print("ambos são falsos")
else: 
    print("um é verdadeiro e o outro é falso")
