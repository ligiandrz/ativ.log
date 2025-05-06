#Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de
#um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na
#tela o resultado. (Base para o Salário mínimo R$ 1.518,00).
S = float(input("digite seu salário:"))
Sminimo =  1.518
QS = S / 1518
QS_arredondado = round(QS)
print("O usuário possui", QS_arredondado,"salarios minimos")
