import os
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
n3=float(input("Digite a terceira nota:"))
os.system("cls")
media=(n1+n2+n3)/3
if media>=7:
    print(f"Media - {media:.2f}\nAprovado.")
elif media>=5:
    print(f"Media - {media:.2f}\nRecuperação.")
else: 
    print(f"Media - {media:.2f}\nReprovado.")