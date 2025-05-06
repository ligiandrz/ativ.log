#Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
for i in range(1, 11):
    print(f"tabuada do {i}:")
    for x in range(1, 11):
        resultado = i * x
        print(f"{i} x {x} = {resultado}")
