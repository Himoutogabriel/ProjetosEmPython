class Conta:
    def __init__(self):
        self.titular=None
        self.numero=''
        self.agencia=''
        self.saldo=0.0
        self.status=False
    
    def deposito(self):
        deposito=float(input("Entre com o valor do deposito:"))
        self.saldo+=deposito

    def saque(self):
        saque=float(input("Entre com o valor do saque:"))
        if self.saldo<saque:
            print("Saldo indisponivel.")
            return
        self.saldo-=saque

    def Status(self):
        self.status=not self.status
 
    def consulta_conta(self):
        print(f"Titular={self.titular.nome}\nIdade={self.titular.idade}\nSaldo={self.saldo}\nStatus={self.status}\nNumero={self.numero}\nAgencia={self.agencia}\n")


