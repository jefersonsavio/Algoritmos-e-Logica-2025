tempo = float(input("Informe o tempo final do atleta: "))
penalidade = input("foi aplicado alguma penalidade? 'sim' ou 'não' ")
classificacao = input("qual classificação do atleta? 'ouro', 'prata' ou 'bronze'")

if tempo < 10.0 and penalidade == "não":
    print("Desempenho excelente: novo recorde pessoal.")
elif tempo < 12.0 or classificacao == "ouro":
    print("Desempenho forte: classificado para a próxima fase.")
elif tempo >= 12.0 and penalidade =="não":
    print("Desempenho regular: precisa de mais treinamento.")
else:
    print("Desempenho insuficiente: desclassificado.")
