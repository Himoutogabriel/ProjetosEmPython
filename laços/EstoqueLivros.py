livros=[
    {'nome':'Hobbit','estoque': 5},
    {'nome':'Batman','estoque': 0},
    {'nome':'Pequeno principe','estoque': 3},
    {'nome':'Invencivel','estoque': 0}
]

for livro in livros:
    if livro["estoque"] > 0:
        print(f"Livro disponível:{livro["nome"]}")