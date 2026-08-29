import random
maiusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscula=maiusculas.lower()
caracteres="!@#$%¨&*()-_=+§"
numeros="0123456789"
tudo=maiusculas+minuscula+caracteres+numeros
senha=""
senha2=""
for i in range(3):
    senha+="".join(random.choice(maiusculas))
    senha+="".join(random.choice(minuscula))
    senha+="".join(random.choice(numeros))
    senha+="".join(random.choice(caracteres))
for i in range(12):
    senha2+="".join(random.choice(tudo))
print(f"Senha aleatoria:{senha}\nSenha mais aleatoria:{senha2}")