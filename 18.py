#Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e
#imprima na tela em quantos anos serão necessários para que Sara seja maior que Francisco.
altfran = 1.50
altsara = 1.10
cfran = 0.02
csara = 0.03
anos = 0
while altsara <= altfran:
    altfran += cfran
    altsara += csara
    anos += 1
print(f"serão necessários {anos} anos para que Sara seja maior que Francisco.")
