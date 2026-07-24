import os
temperatura=int(input("Digite a temperatura:"))
os.system("cls")
if temperatura>25:
    print("Alerta, temperatura acima do esperado!")
elif temperatura<5:
    print("Muito frio!")
else: 
    print("Temperatura no esperado.")