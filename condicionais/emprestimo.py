import os
renda=float(input("Digite o valor da renda:"))
parcela=float(input("Digite o valor da parcela:"))
os.system("cls")
if renda>2000 and parcela<(30/100)*renda:
    print("Empréstimo aprovado.")
elif renda<=2000:
    print("Renda inferior a 2000.\nEmpréstimo reprovado.")
else:
    print("Empréstimo reprovado.\nParcela maior que 30% da renda")
    