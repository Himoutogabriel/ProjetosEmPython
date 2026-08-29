produtos=input("Entre com os produtos:").split()
valores=map(float,input("Entre com os valores: ").split())
lista=zip(produtos,valores)
for i in lista:
    print(list(i))
    
    