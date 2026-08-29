print("==============\nCALCULADORA\n==============")

A = int(input("Entre com um valor para A: "))
B = int(input("Entre com um valor para B: "))
op = input("Qual operação deseja realizar?\n")
if op=='+':
    resu=A+B
    print(f"Resultado: {resu}")
elif op=='-':
    resu=A-B
    print(f"Resultado: {resu}")
elif op=='*':
    resu=A*B
    print(f"Resultado: {resu}")
elif op=='/':
    resu=A/B
    print(f"Resultado: {resu}")
else:
    print("Opção inválida.")
