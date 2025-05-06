#Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.
nota1 = int(input("insira sua nota 1:"))
nota2 = int(input("insira sua nota 2:"))
nota3 = int(input("insira sua nota 3:"))
media = ( nota1 + nota2 + nota3 ) / 3
print(f"a sua média final é:{media:.1f}")
