print("\nSOMA DE IMPARES\n")
n=int(input("Entre com o tamanho do intervalo:"))
soma = 0
for i in range(n):
    if i%2==1:
        soma+=i
print(soma)