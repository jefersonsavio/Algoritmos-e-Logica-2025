print("Calculando salario com impostos")

salario_fixo = float(input("Informe o salario fixo: "))
comissao_produto = float(input("Informe a comissão por produto: "))
quantidade_produtos = float(input("Informe a quantidade de produtos vendidos: "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

print(f"Salario total: {salario_total:.2f}")




if salario_total < 5000:
    imposto = salario_total * 0.16
    
else:
    imposto = salario_total * 0.27
    
print(F"Salario com desconto do imposto: {salario_total - imposto}")
    