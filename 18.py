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