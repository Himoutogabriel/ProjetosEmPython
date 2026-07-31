import random, os
numero_secreto=random.randint(1,100)
tentativas=0
print("Boas vindas ao jogo do número secreto!\nTente descobrir qual o numero secreto entre 1 e 100!")
while(True):
    tentativa=int(input("Chute um valor:"))
    os.system("cls")
    tentativas+=1
    if tentativa==numero_secreto:
        print(f"Parabéns, você acertou\nNumero secreto:{numero_secreto}\nTentativas:{tentativas}")
        break
    elif tentativa<numero_secreto:
        print("Tente novamente, seu numero é menor que o numero secreto.")
    else: 
        print("Tente novamente, seu numero é maior que o numero secreto.")
    