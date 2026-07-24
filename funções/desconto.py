def calculo(valor,desconto):
    valor_final=valor-(valor*(desconto/100))
    return valor_final
valor=float(input("Entre com o valor do produto:"))
desconto=float(input("Entre com o desconto do produto:"))
resultado=calculo(valor,desconto)
print("Valor final é",resultado)