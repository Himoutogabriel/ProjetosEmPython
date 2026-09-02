import os, psycopg2
conexao=psycopg2.connect(
    host='localhost',
    database='despensa',
    user='postgres',
    password='22800305@TRT',
    port='5432'
)

cursor=conexao.cursor()

class Item:
    def __init__(self, nome, codigo, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
    def __str__(self):
        return f"Nome={self.nome}\nCodigo={self.codigo}\nQuantidade={self.quantidade}"
    
itens=[]
cursor.execute("SELECT * FROM produtos")
dados=cursor.fetchall()
for dado in dados:
    item=Item(dado[0],dado[1],dado[2])
    itens.append(item)

def buscar():
    os.system("cls")
    busca=int(input("Qual item deseja buscar?\nObs:Realize a busca pelo codigo\n"))
    for i in itens:
        if busca==i.codigo:
            print(f"Item encontrado!\nNome={i.nome}\nCodigo={i.codigo}\nQuantidade={i.quantidade}")
            break
    else:
        print("Item não encontrado!")

def adicionar():
    os.system("cls")
    nome=input("Entre com o nome do produto: ")
    codigo=int(input("Entre com o codigo do produto: "))
    quantidade=int(input("Entre com a quantidade do produto: "))
    itens.append(Item(nome,codigo,quantidade))
    cursor.execute(
        "INSERT INTO produtos (nome,codigo,quantidade) VALUES (%s,%s,%s)",
        (nome,codigo,quantidade)
    )
    conexao.commit()
    print("Produto adicionado!\n")

def remover():
    os.system("cls")
    remove=int(input("Entre com o codigo do produto que deseja remover: "))
    for i in itens:
        if remove==i.codigo:
            itens.remove(i)
            cursor.execute(
                "DELETE FROM produtos WHERE codigo = %s",
                (remove,)
            )
            conexao.commit()
            print("Produto removido!\n")
            break
            
def imprimir():
    os.system("cls")
    print("DESPENSA:\n")
    for i in itens:
        print(i)
        print("\n")
def atualizar():
    codigo=int(input("Entre com o codigo do produto que deseja atualizar a quantidade: "))
    quantidade=int(input("Entre com a quantidade nova: "))
    print("Produto atualizado!\n")
    for i in itens:
        if i.codigo==codigo:
            i.quantidade=quantidade
            cursor.execute(
                    "UPDATE produtos SET quantidade = %s WHERE codigo = %s",
                    (quantidade,codigo)
                    )
            conexao.commit()
    
while(True):
    print("Boas vindas a despensa!\n")
    op=int(input("Oque deseja realizar?\n1-Buscar item\n2-Adicionar item\n3-Remover item\n4-Mostrar itens\n5-Atualizar Quantidade\n6-Sair\n"))
    if op==1:
        buscar()
    elif op==2:
        adicionar()
    elif op==3:
        remover()
    elif op==4:
        imprimir()
    elif op==5:
        atualizar()
    elif op==6:
        exit(True)
    else:
        print("Opção inválida. Encerrando...")
        exit(True)


