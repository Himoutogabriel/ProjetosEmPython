def soma(numero):
    if numero==1:
        return 1
    return numero + soma(numero-1)
numero=int(input("Entre com um numero:"))
print(soma(numero))