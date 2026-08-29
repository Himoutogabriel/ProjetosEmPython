print("================\nLOGIN DE USUÁRIO\n================")

usuario = "Gabriel"
senha = "Elpepe45"
usuario_tentativa = input("Entre com o usuário: ")
senha_tentativa = input("Entre com a senha: ")
if usuario == usuario_tentativa and senha == senha_tentativa:
    print("Login aprovado.\n")
elif usuario == usuario_tentativa and senha != senha_tentativa:
    print("Usuário encontrado\nSenha incorreta.\n")
else:
    print("Usuário não encontrado.\n")