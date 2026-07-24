estoque=int(input("Qual o estoque do produto?"))
for i in range(estoque):
    estoque-=1
    if estoque==0:
        print("Esgotado!")
        break
    print(f"Venda realizada!\nEstoque:{estoque}")
    