cedulas=[200,100,50,20,10,5,2]
moedas=[1,0.5,0.25,0.10,0.05,0.01]
saque=float(input("Entre com o valor de saque:"))

for i in cedulas:
    qnt = int(saque // i)
    saque = round(saque % i, 2)
    print(f"{qnt} de cedula de {i}")
print()
for i in moedas:
    qnt = int(saque // i)
    saque = round(saque % i, 2)
    print(f"{qnt} de cedula de {i}")