import os
def criarCPF():
    cpf=input("Entre com o cpf:")
    cpf_valor=[]
    os.system("cls")
    for i in cpf:
        if i.isdigit():
            cpf_valor.append(int(i))
    print(cpf_valor)
    return cpf_valor
def verificarCPF(cpf_valor):
    cont = 10
    digito1 = 0

    for i in cpf_valor[:9]:
        digito1 += i * cont
        cont -= 1

    resto1 = digito1 % 11

    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1


    cont = 11
    digito2 = 0

    for i in cpf_valor[:9] + [digito1]:
        digito2 += i * cont
        cont -= 1

    resto2 = digito2 % 11

    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2


    if digito1 == cpf_valor[9] and digito2 == cpf_valor[10]:
        print("CPF verificado, está correto.")
    else:
        print("CPF verificado, está incorreto.")
cpf=criarCPF()
verificarCPF(cpf)