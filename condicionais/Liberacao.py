horas=int(input("Entre com o horário(formato 24 horas):"))
if horas>=8 and horas<=18:
    print("Acesso liberado.")
else:
    print("Acesso negado.")