import os
from dataclasses import dataclass
@dataclass

class Produto:
    codigo:int
    nome:str
    valor:float
    estoque:int
produtos=[]

def buscar():
    busca=int(input("Entre com o codigo do item que deseja buscar:"))
    os.system("cls")
    for i in range(len(produtos)):
        if busca==produtos[i].codigo:
            print(f"Produto do código:({produtos[i].codigo}) encontrado!")
            return 1
    print(f"Produto do codigo :({produtos[i].codigo}) não encontrado.")
    return 0

def vendas():
    venda=[]
    total=0
    while(True):
        busca=int(input("Qual produto deseja adicionar na venda?\n"))
        os.system("cls")
        for i in range(len(produtos)):
            if busca==produtos[i].codigo:
                if produtos[i].estoque>0:
                    venda.append({
                        "nome": produtos[i].nome,
                        "valor": produtos[i].valor
                    })
                    total+=produtos[i].valor
                    produtos[i].estoque-=1
                    break
                else:
                    print("Não tem estoque desse produto.")
                    break
        op=int(input("Deseja fechar a venda?\n0-Não\n1-Sim\n"))
        os.system("cls")
        if op==1:
            for i in range(len(venda)):
                print(f"Produto({i+1})-Nome:{venda[i]['nome']} Valor:{venda[i]['valor']}\n")
            print(f"Valor da venda: {total}")
            break

def cadastrar_produto():
    codigo=int(input("Entre com o codigo do produto:"))
    nome=input("Entre com o nome do produto:")
    valor=float(input("Entre com o valor do produto:"))
    estoque=int(input("Entre com a quantidade do estoque:"))
    p=Produto(codigo,nome,valor,estoque)
    produtos.append(p)
    os.system("cls")
    print("Produto cadastrado com sucesso!")
    
def remover_produto():
    remove=int(input("Entre com o codigo do produto que deseja remover:"))
    for i in range(len(produtos)):
        if remove==produtos[i].codigo:
            produtos.pop(i)
            print("Produto removido com sucesso.")
            break
        
print("====================================\nBOAS VINDAS AO MERCADINHO DO CABRAL!\n====================================\n")
while(True):
    op=int(input("1-Cadastro de produto\n2-Buscar\n3-Venda\n4-Remover produto\n5-Imprimir produtos\n6-Sair do sistema\nDigite a operação que deseja realizar:"))
    os.system("cls")
    if op==1:
        cadastrar_produto()
    elif op==2:
        buscar()
    elif op==3:
        vendas()
    elif op==4:
        remover_produto()
    elif op==5:
        for produto in produtos:
            print(produto)
            print("\n")
    elif op==6:
        break
    else:
        print("Erro - Opção incorreta")