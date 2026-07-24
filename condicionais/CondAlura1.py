import os
vendas_m=int(input("Digite a quantidade de maças vendidas:"))
vendas_b=int(input("Digite a quantidade de bananas vendidas:"))
os.system("cls")
if vendas_b>vendas_m:
    print(f"Vendeu mais bananas.\nQuantidade:{vendas_b}.")
elif vendas_b<vendas_m:
    print(f"Vendeu mais maças.\nQuantidade:{vendas_m}.")
else:
    print("Empate.")