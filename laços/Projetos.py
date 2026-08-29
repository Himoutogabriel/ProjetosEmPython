lista_projetos=["website", "jogo", "análise de dados", None, "aplicativo móvel"]
i=0
for projeto in lista_projetos:
    if projeto==None:
        lista_projetos[i]='Projeto ausente'
    i=i+1
for projeto in lista_projetos:
    print(projeto)