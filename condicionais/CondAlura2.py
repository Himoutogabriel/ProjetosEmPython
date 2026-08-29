import os
AtividadeA=int(input("Informe os dias necessários para concluir a atividade A:"))
AtividadeB=int(input("Informe os dias necessários para concluir a atividade B:"))
AtividadeC=int(input("Informe os dias necessários para concluir a atividade C:"))
os.system("cls")
if AtividadeA<0 or AtividadeB<0 or AtividadeC<0:
    print("Erro: Tempo negativo é inválido.")
else:
    tempo=AtividadeC+AtividadeB+AtividadeA
    print(f"Tempo total:{tempo} dias")