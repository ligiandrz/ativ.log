#Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na
#tela quantos anos, meses e dias essa pessoa ja viveu. Leve em
#consideração o ano com 365 dias e o mês com 30 dias.
#(Ex: 5 anos, 2 meses e 15 dias de vida)
ano_nascimento = int(input("digite o ano em que você nasceu: "))
ano_atual = int(input("digite o ano atual: "))
anos_vivid = ano_atual - ano_nascimento
dias_vivid = anos_vivid * 365
meses_vivid = (dias_vivid // 30)
dias_sobra = dias_vivid % 30
anos = meses_vivid // 12
meses_resto = meses_vivid % 12
print(f"Você viveu {anos} anos, {meses_resto} meses e {dias_sobra} dias.")
