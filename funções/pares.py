numeros=map(int,input("Digite os valores: ").split())
pares = filter(lambda x: x%2==0, numeros)
print(list(pares))