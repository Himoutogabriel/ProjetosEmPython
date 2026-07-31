import os
conta=float(input("Entre com o valor total:"))
gorjeta_porc=float(input("Entre com a porcentagem da gorjeta:"))
os.system("cls")
gorjeta=conta*(gorjeta_porc/100)
total=gorjeta+conta
print(f"Valor da gorjeta = {gorjeta}\nValor total da conta = {total}")