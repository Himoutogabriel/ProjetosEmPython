livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
busca=input("Qual livro deseja buscar?")
for livro in livros:
    if busca==livro:
        print("Livro encontrado!")
        busca='S'
if busca!='S':
    print("Livro não encontrado.")

    
    