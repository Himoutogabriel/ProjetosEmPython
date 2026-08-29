print("================\nPLANO CARTESIANO\n================\n")

x = float(input("Entre com a coordenada X:"))
y = float(input("Entre com a coordenada Y:"))

if x == 0 and y == 0:
    print("Nulo.\n")
elif x == 0:
    print("Ordenada.\n")
elif y == 0:
    print("Abscissa.\n")
elif x > 0 and y > 0:
    print("Primeiro quadrante.\n")
elif x > 0 and y < 0:
    print("Quarto quadrante.\n")
elif x < 0 and y > 0:
    print("Segundo quadrante.\n")
else:
    print("Terceiro quadrante.\n")