valores = []
for i in range(3):
    while True:
        try:
            valor = int(input(f"digite o {i + 1}º valor: "))
            if valor not in valores:
                valores.append(valor)
                break
            else:
                print("valor já foi digitado. Por favor, digite um valor diferente.")
        except ValueError:
            print("entrada inválida. Por favor, digite um número inteiro.")

valores.sort(reverse=True)
print("valores em ordem decrescente:", valores)