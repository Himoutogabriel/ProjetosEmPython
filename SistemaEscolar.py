print("==================\nCadastro de alunos\n==================\n")
import os
from dataclasses import dataclass

@dataclass

class Aluno:
    nome:str
    matricula:str
    ano:int
    n1:int
    n2:int
aluno1=Aluno
def inserir():
    aluno1.nome=input("Nome do aluno:")
    aluno1.matricula=input("Matricula do aluno:")
    aluno1.ano=int(input("Ano da matricula do aluno:"))
    aluno1.n1=int(input("n1 do aluno:"))
    aluno1.n2=int(input("n2 do aluno:"))
    os.system("cls")
def buscar():
    busca=input("Entre com a matricula:")
    if busca==aluno1.matricula:
        print("Aluno encontrado!")
    else:
        print("Aluno não encontrado.")
def remover():
    aluno1.nome=None
    aluno1.matricula=None
    aluno1.ano=None
    aluno1.n1=None
    aluno1.n2=None
def media():
    media=(aluno1.n1+aluno1.n2)/2
    print(media)
    return media
def resultado(MediaAluno):
    if MediaAluno>=6:
        print("Aprovado!")
    else:
        print("Reprovado.")
def main():
    print("Boas vindas ao sistema escolar!\n")
    while(True):
        print("O que deseja realizar?\n1-Inserir aluno.\n2-Buscar aluno.\n3-Remover aluno\n4-Media do aluno.\n5-Resultado final.\n6-Sair.\n")
        op = int(input())
        os.system("cls")
        try:
            if op==1:
                inserir()
            elif op==2:
                buscar()
            elif op==3:
                remover()
            elif op==4:
                MediaAluno=media()
            elif op==5:
                resultado(MediaAluno)
            elif op==6:
                print("Encerrando programa...")
                return
        except:
            print("Opção inválida.")
if __name__=="__main__":
    main()
