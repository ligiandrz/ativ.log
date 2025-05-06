#Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi 
#aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final
#deve ser maior ou igual a 7.
nome = input("insira seu nome:")
nota1 = int(input("insira sua nota 1:"))
nota2 = int(input("insira sua nota 2:"))
nota3 = int(input("insira sua nota 3:"))
nota4 = int(input("insira sua nota 4:"))
media = ( nota1 + nota2 + nota3 + nota4) / 4
if media >= 7 :
 print(f"Parabens {nome}! você foi aprovado(a) :D")
elif media < 7 :
 print(f"{nome} foi reprovado(a) :(")
