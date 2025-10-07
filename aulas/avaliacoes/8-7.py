# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! ALELUIA!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

pureza = float(input("Informe a pureza do lote: "))
massa = int(input("Informe a massa  do lote em kg: "))
taxa_contaminacao = float(input("informe a taxa de contaminação do lote: "))
FD = (pureza * 100) - (taxa_contaminacao * 50)
if massa >1000:
    P_base =10
else:
    P_base = 12.50
if FD > 90 and pureza >0.98:
    print("Classificação: PREMIUM Venda Imediata")
    P_final_kg = P_base * 1.50
elif FD > 70 and FD <= 90 and taxa_contaminacao < 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    P_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    P_final_kg = P_base * 0.90 
Preco_Total= P_final_kg * massa
print(f"Preço base por kg: {P_base}")
print(f"Preço total para o lote: {Preco_Total}")
