voluntarios=[]
while(True):
    entrada=input("Digite o voluntario para entrada ou 'sair' para sair: ")
    if entrada == 'sair':
        print(voluntarios)
        break
    else:
        voluntarios.append(entrada)