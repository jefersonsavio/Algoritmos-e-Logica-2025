from tkinter.tix import InputOnly


renda_mensal = float(input("Informe a renda mensal: "))
score = int(input("Informe o score de crédito:"))
tempo = int(input("Informe quantos anos de trabalho: "))

if renda_mensal >= 3000 and tempo >= 2:
    if score >= 700 and score <= 1000:
        print("Aprovado com baixa taxa de juros")
    else:
        print("Empréstimo aprovado, mas com alta taxa de juros!")
else:
    print("Não aprovado: Renda ou tempo de serviço insuficientes!")
