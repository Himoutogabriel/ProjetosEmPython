import os
string=input("Entre com o texto:")
contVogal=0
vogais=['a','e','i','o','u']
string.lower()
for i in string:
    for j in vogais:
        if i==j:
            contVogal+=1
os.system("cls")
print(f"Quantidade de vogais no texto: {contVogal}")