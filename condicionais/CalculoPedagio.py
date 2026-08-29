import os
kilometragem=float(input("Digite a distância percorrida:"))
os.system("cls")
if kilometragem>200:
    print("Valor do pedágio: R$ 30,00")
elif kilometragem>100:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 10,00")