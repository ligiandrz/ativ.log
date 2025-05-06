peso = int(input("insira seu peso:"))
altura = float(input("insira sua altura:"))
imc = peso / ((altura / 100)**2)
if imc <=18.5:
    print("você está abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("você está com o peso ideal!:D")
elif 25.0 <= imc <= 29.9:
    print("você está levemente acima do peso")
elif 30.0 <= imc <= 34.9:
    print("você está com obesidade grau I")
elif 35.0 <= imc <= 39.9:
    print("você está com grau II (severa)")
else:
    print("você está com obesidade grau III (mórbida)")