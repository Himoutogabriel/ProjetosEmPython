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
    for i in range(len(produtos)):
        if busca==produtos[i].codigo:
            print("Produto encontrado!")
            return 1
    print("Produto não encontrado.")
    return 0

def vendas():
    venda=[]
    total=0
    while(True):
        busca=int(input("Qual produto deseja adicionar na venda?"))
        for i in range(len(produtos)):
            if busca==produtos[i].codigo:
                if produtos[i].estoque>0:
                    venda.append(produtos[i].nome)
                    total+=produtos[i].valor
                    produtos[i].estoque-=1
                    break
        op=int(input("Deseja fechar a venda?\n0-Não\n1-Sim"))
        if op==1:
            print(venda)
            print(f"Valor da venda: {total}")
            break

def cadastrar_produto():
    codigo=int(input("Entre com o codigo do produto:"))
    nome=input("Entre com o nome do produto:")
    valor=float(input("Entre com o valor do produto:"))
    estoque=int(input("Entre com a quantidade do estoque:"))
    p=Produto(codigo,nome,valor,estoque)
    produtos.append(p)
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
        print(produtos)
    elif op==6:
        break
    else:
        print("Erro - Opção incorreta")
    