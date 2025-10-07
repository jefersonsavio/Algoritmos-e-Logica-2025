# Jeferson Cristiano Sávio
# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! FAI NA ROU!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

peso = float(input("Informe o peso em kg: "))
distancia = float(input("Informe a distância em km: "))

custo = (peso*1.5) + (distancia * 0.25)
taxa = 5
print(custo)
if custo >= 200 :
    custo *0.1
    print(f"O custo da entrega terá 10% de deconto: {custo}")
elif custo > 50 and custo < 200:
    print(f"O custo da entrega será: {custo}")
else:
    print("Taxa adicional de 5,00 reais no preço final")
    print(f"O custo da entrega será: {custo + taxa}")


