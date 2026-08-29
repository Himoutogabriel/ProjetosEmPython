import os
def saudacoes(hora):
    if hora>18:
        print("Boa noite!")
    elif hora>12:
        print("Boa tarde!")
    else:
        print("Bom dia!")
hora=int(input("Digite a hora do dia:"))
os.system("cls")
saudacoes(hora)