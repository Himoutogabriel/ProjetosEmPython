class carro:
    def __init__(self,nome,ano,cor):
        self.nome = nome
        self.ano = ano
        self.cor = cor
    def __str__(self):
        return f"{self.nome}, {self.ano}, {self.cor}"
carro1=carro("hb20",2025,"preto")
print(carro1)