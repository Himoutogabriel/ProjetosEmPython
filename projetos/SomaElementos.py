def somas():
    lista = [1,2,3,4,5,6,7,8,9,10]
    soma = 0
    try:
        for i in lista:
            soma+=i
        print(soma)
    except Exception as e:
        print("Deu ruim.")
def media():
    lista = [1,2,3,4,5,6,7,8,9,10]
    soma = 0
    try:
        for i in lista:
            soma+=i
        media=soma/len(lista)
        print(media)
    except Exception as e:
        print("Deu ruim.")
somas()
media()
