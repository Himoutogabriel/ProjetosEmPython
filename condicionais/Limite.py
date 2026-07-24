import os
limite=3000.0
despesas=float(input("Entre com o valor total das despesas:"))
if despesas>limite:
    print("Você ultrapassou o limite.")
else:
    print("Você gastou menos que o limite.")