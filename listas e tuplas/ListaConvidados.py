Convidados=['Joao','Maria','Jose']
while(True):
    entrada=input("Entre com o nome do convidado ou 'sair' para sair:")
    if entrada=='sair':
        print(Convidados)
        break
    else:
        posição=int(input("Qual posição deseja colocar:"))
        Convidados.insert(posição,entrada)
print(Convidados)
