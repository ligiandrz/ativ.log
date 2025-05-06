#Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade.
nome = input("insira seu nome:")
idade = int(input("insira sua idade:"))
if idade <= 17 :
 print(f"{nome} é menor de idade")
elif idade >18 :
 print(f"{nome} é maior de idade")
