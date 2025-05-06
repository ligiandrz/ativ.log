valor_produto = float(input("digite o valor do produto: "))
print("escolha a forma de pagamento:")
print("a vista em dinheiro ou pix (15% de desconto)")
print("a vista no cartao de credito (10% de desconto)")
print("parcelado no cartao em duas vezes (sem juros)")
print("parcelado no cartao em tres vezes ou mais (10% de juros)")
codigo_pagamento = int(input("digite o codigo: "))
valor_final = 0
if codigo_pagamento == 1:
    valor_final = valor_produto * 0.85 
elif codigo_pagamento == 2:
    valor_final = valor_produto * 0.90 
elif codigo_pagamento == 3:
    valor_final = valor_produto
elif codigo_pagamento == 4:
    valor_final = valor_produto * 1.10 
else:
    print("codigo de pagamento invalido.")
if codigo_pagamento in [1, 2, 3, 4]:
    print(f"O valor final a ser pago é: R$ {valor_final:.2f}")