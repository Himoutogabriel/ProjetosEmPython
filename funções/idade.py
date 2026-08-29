import os
def calc_idade(ano_nasc,ano):
    idade=ano-ano_nasc
    return idade
ano_nasc=int(input("Digite o seu ano de nascimento:"))
ano=int(input("Digite o ano atual:"))
os.system("cls")
idade=calc_idade(ano_nasc,ano)
print(f"Sua idade é {idade}")