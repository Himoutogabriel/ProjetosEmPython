while(True):
    usuario=input("Crie o nome de usuário:")
    if len(usuario)<5:
        print("O nome do usuario deve ter pelo menos 5 caracteres")
        continue
    else:
        break
while(True):
    senha=input("Crie uma senha:")
    if len(senha)<8:
        print("A senha deve conter pelo menos 8 caracteres")
        continue
    else:
        break