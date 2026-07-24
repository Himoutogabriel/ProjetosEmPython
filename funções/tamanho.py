import os
def tamanho(palavra):
    return len(palavra)
palavra=input("Digite uma palavra:")
tamanho_p=tamanho(palavra)
os.system("cls")
print(f"A palavra ({palavra}) tem {tamanho_p} caracteres.")