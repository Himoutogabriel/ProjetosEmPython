alunos=[]
qtd=int(input("Quantos alunos deseja inserir? "))
for i in range(qtd):
    dados=input("Digite os dados no formato (nome idade nota) separando por virgula: ")
    nome,idade,nota=dados.split(',')
    aluno={"nome":nome,"idade":int(idade),"nota":float(nota)}
    alunos.append(aluno)
for i in range(qtd):
    print(alunos[i])