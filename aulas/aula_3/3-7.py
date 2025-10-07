print("Calculando a média")

nota_trabalho = float(input("Insira a nota do trabalho: "))
nota_seminario = float(input("Insira a nota do seminário: "))
nota_prova = float(input("Insira a nota da prova: "))
nota_artigo = float(input("Insira a nota do artigo: "))

media = nota_trabalho*0.2 + nota_seminario * \
    0.3 + nota_prova*0.3 + nota_artigo*0.2

print(f"A média final é: {media}")
