valor_produto = float(input("Digite o valor do produto: "))
porcentagem_imposto =  float(input("Digite a porcentagem do imposto: "))

valor_imposto = valor_produto * (porcentagem_imposto / 100)

valor_total = valor_produto + valor_imposto

print(f"O valor total do produto com imposto será: {valor_total}")