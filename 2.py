#Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
numero = float(input("insira um numero:"))
if numero % 2 == 0 :
    parouimpar = "par" 
else :
    parouimpar = "impar"

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "zero"
print(f"o numero é {parouimpar} e {sinal}.")

