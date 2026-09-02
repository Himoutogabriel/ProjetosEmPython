estoque1=[]
estoque2=[]
total=[]
while(True):
    entrada=input("Digite o produto para o estoque ou 'sair' para sair:")
    if entrada=='sair':
        print(f"Estoque 1={estoque1}")
        break
    else:
        estoque1.append(entrada)
while(True):
    entrada=input("Digite o produto para o estoque ou 'sair' para sair:")
    if entrada=='sair':
        print(f"Estoque 2={estoque2}")
        break
    else:
        estoque2.append(entrada)
total=estoque1+estoque2
print(f"Estoques combinados={total}")