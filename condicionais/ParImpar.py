print("=======================\nVERIFICADOR DE PARIDADE\n=======================")

valor = int(input("Entre com um valor:"))
if valor==0:
    print("É nulo.\n")
elif valor%2==1:
    print("É ímpar.\n")
elif valor%2==0:
    print("É par.\n")