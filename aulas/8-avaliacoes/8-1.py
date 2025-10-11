
# Jeferson Cristiano Sávio
# R.A 0220482523029
# Diga olá para o fatecando mais dedicado!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

custo = float(input("Insira o preço de custo: "))
venda = float(input("Insira o valor de venda: "))
lucro = venda - custo
margem = (lucro/ custo)*100
if margem >= 30 :
    print("Margem Excelente!")
elif margem >10 and  margem < 30 :
    print("Margem Satisfatória.")
else :
    print("Margem Baixa: Avaliar preço de venda.")
