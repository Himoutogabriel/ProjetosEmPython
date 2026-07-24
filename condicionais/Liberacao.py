import os
horas=int(input("Entre com o horário(formato 24 horas):"))
os.system("cls")
if horas>=8 and horas<=18:
    print("Acesso liberado.")
else:
    print("Acesso negado.")