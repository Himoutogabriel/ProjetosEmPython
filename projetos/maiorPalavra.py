texto=input("Digite um texto:")
palavras=texto.split()
maior=palavras[0]
for i in palavras:
    if len(maior)<len(i):
        maior=i
print(f"Maior palavra do texto:{maior}")