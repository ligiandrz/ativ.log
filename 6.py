#Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de
#um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na
#tela o resultado. (Base para o Salário mínimo R$ 1.518,00).
valor = float(input("Digite um valor: "))
reajuste = valor * 0.05
novo_valor = valor + reajuste
print(f"O valor com reajuste de 5% é: {novo_valor}")
