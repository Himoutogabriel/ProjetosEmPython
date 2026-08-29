import random
escolhas=["Pedra","Papel","Tesoura"]
escolha_maquina=random.choice(escolhas)
escolha_maquina=escolha_maquina.lower()
escolha_user=input("Jogue pedra, papel ou tesoura? ")
escolha_user=escolha_user.lower()
if escolha_maquina==escolha_user:
    print(f"Empate!\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
elif escolha_user=="pedra":
    if escolha_maquina=="papel":
        print(f"Você perdeu! {escolha_maquina} vence {escolha_user}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
    elif escolha_maquina=="tesoura":
        print(f"Você venceu! {escolha_user} vence {escolha_maquina}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
        
elif escolha_user=="papel":
    if escolha_maquina=="tesoura":
        print(f"Você perdeu! {escolha_maquina} vence {escolha_user}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
    elif escolha_maquina=="pedra":
        print(f"Você venceu! {escolha_user} vence {escolha_maquina}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
        
elif escolha_user=="tesoura":
    if escolha_maquina=="pedra":
        print(f"Você perdeu! {escolha_maquina} vence {escolha_user}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")
    elif escolha_maquina=="papel":
        print(f"Você venceu! {escolha_user} vence {escolha_maquina}\nOpção usuario:{escolha_user}\nOpção maquina:{escolha_maquina}")