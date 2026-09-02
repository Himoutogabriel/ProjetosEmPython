import psycopg2
conexao=psycopg2.connect(
    host="localhost",
    database="teste",
    user="postgres",
    password="22800305@TRT",
    port="5432"
)

i=0
cursor=conexao.cursor()
while(i<3):
    nome=input("Entre com o nome do usuário: ")
    idade=input("Entre com a idade do usuário: ")
    cursor.execute(
        "INSERT INTO teste (nome,idade) VALUES(%s,%s)",
        (nome,idade)
    )
    conexao.commit()
    i+=1

cursor.close()
conexao.close()