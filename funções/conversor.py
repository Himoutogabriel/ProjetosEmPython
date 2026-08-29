def conversor(telefones):
    i=0
    for t in telefones:
        telefones[i]=int(t)
        i+=1
    return telefones
def verificador(telefones):
    for t in telefones:
        if type(t)!=int:
            print("Valores não convertidos.")
            return
    print("Valores convertidos")
    
telefones = ["11987654321", "21912345678", "31987654321"]
conversor(telefones)
verificador(telefones)