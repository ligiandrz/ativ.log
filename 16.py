#Faça um algoritmo que leia três valores que representam os três lados de
#um triângulo e verifique se são válidos, determine se o triângulo é equilátero,
#isósceles ou escaleno.
lado1 = float(input("digite o comprimento do primeiro lado:"))
lado2 = float(input("digite o comprimento do segundo lado:"))
lado3 = float(input("digite o comprimento do terceiro lado:"))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("o triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("o triângulo é isósceles.")
    else:
        print("o triângulo é escaleno.")
else:
    print("os valores fornecidos não formam um triângulo válido.")
