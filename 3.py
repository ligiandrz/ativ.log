#- Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e
#B forem iguais, deverá somar os dois valores, caso contrário devera multiplicar
#A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a
#uma variável C e imprimir seu valor na tela.
valorA =int(input("insira o valor A:"))
valorB =int(input("insira o valor B;"))
if valorA == valorB :
   soma = valorA + valorB
else :
  valorC = valorA * valorB
print("O valor de C é:", valorC)
