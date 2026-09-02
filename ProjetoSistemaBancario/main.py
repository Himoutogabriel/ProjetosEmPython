from ClasseCliente import Cliente
from ClasseConta import Conta
import random,os

cliente=Cliente()
conta=Conta()
print("=====================")
print("=Cadastro do Cliente=")
print("=====================\n")
cliente.cpf=input("Entre com o cpf do cliente: ")
cliente.nome=input("Entre com o nome do cliente: ")
cliente.data_nascimento=input("Entre com a data de nascimento do cliente: ")
cliente.cep=input("Entre com o cep do cliente(apenas numeros): ")
cliente.idade=cliente.calculo_idade()
os.system("cls")
    
print("Cadastro de Conta.")

conta.titular = cliente

numero_conta=[]
for i in range(6):
    numero_conta.append(random.randint(0,9))
numero_conta.append('-')
numero_conta.append((numero_conta[0]*2+numero_conta[1]*3+numero_conta[2]*4+numero_conta[3]*5+numero_conta[4]*6+numero_conta[5]*7)%10)
numero_conta=''.join(map(str,numero_conta))
conta.numero=numero_conta

numero_agencia=[]
for i in range(4):
    numero_agencia.append(random.randint(0,9))
numero_agencia=''.join(map(str,numero_agencia))
conta.agencia=numero_agencia

while(True):
    op2=int(input("Oque deseja realizar?\n\n1-Saque\n2-Deposito\n3-Consulta conta\n4-Consulta dados\n5-Alterar status\n6-Sair\n"))
    if op2==1:
        conta.saque()
    elif op2==2:
        conta.deposito()
    elif op2==3:
        conta.consulta_conta()
    elif op2==4:
        conta.titular.consulta_dados()
    elif op2==5:
        conta.Status()
    elif op2==6:
        break
    else:
        print("Opção inválida. \nEncerrando...")
        exit(True) 
#coisas pra alterar: integrar postgresql, encapsulamento, arrumar impressão de numero da conta e agencia, deixar mais bonito