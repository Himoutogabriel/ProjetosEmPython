import os
print("BOAS VINDAS AO GERENCIADOR DE TAREFAS!\n")
lista =[]
def adicionar(lista):
    os.system("cls")
    tarefa=input("Escreva o nome da tarefa:")
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")
def remover(lista):
    os.system("cls")
    tarefa=input("Escreva o nome da tarefa:")
    for i in range(len(lista)):
        if lista[i]==tarefa:
            lista.remove(lista[i])
            print("Tarefa removida com sucesso.")
            return 
    print("Erro - Tarefa não encontrada")
def atualizar(lista):
    os.system("cls")
    tarefa=input("Escreva o nome da tarefa:")
    for i in range(len(lista)):
        if lista[i]==tarefa:
            lista[i]=input("Digite a tarefa nova:")
            print("Tarefa atualizada com sucesso")
            return 
    print("Erro - Tarefa não encontrada")
    
def imprimir(lista):
    os.system("cls")
    if not lista:
        print("Lista vazia.")
    else:
        for i in range(len(lista)):
            print(f"Tarefa({i+1}) - {lista[i]}")
while(True):
    op=int(input("Qual operação desejar realizar?\n1-Adicionar tarefa\n2-Remover tarefa\n3-Atualizar tarefa\n4-Imprimir lista\n5-Sair do gerenciador\n"))
    if op==1:
        adicionar(lista)
    elif op==2:
        remover(lista)
    elif op==3:
        atualizar(lista)
    elif op==4:
        imprimir(lista)
    elif op==5:
        break
    else:
        print("Opção inválida, tente novamente")

    