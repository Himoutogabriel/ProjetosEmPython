print("=====================\nVERIFICADOR DE IDADES\n=====================")

idade=int(input("Entre com a idade: "))
if idade >=0 and idade <=12:
    print("É criança.\n")
elif idade >=13 and idade <=18:
    print("É adolescente.\n")
elif idade > 18:
    print("É adulto.\n")
else:
    print("Ínvalido.\n")