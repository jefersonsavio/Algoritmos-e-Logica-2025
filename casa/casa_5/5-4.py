print("Calculando investimentos")

valor_presente = float(input("Informe o valor atual: "))
taxa_juros = float(input("Informe a taxa de juros: "))
anos = int(input("Quantos anos renderá o investimento? "))

valor_futuro = valor_presente / (1 + taxa_juros)**anos

print(f"O rendimento do investimento é: {valor_futuro}")

if valor_futuro < 30000:
    print("O valor deve ser investido em bens não duráveis")
else: 
    print("valor deve ser investido em renda fixa superior a 24 meses")