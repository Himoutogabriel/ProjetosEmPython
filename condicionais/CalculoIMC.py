import os
peso=float(input("Entre com o peso:"))
altura=float(input("Entre com a altura:"))
imc=peso/(altura**2)
os.system("cls")
if imc<18.5:
    print(f"IMC-{imc:.2f}\nAbaixo do peso.")
elif imc>=18.5 and imc<25:
    print(f"IMC-{imc:.2f}\nPeso normal.")
elif imc>=25:
    print(f"IMC-{imc:.2f}\nAcima do peso.")