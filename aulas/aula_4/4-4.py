salario_fixo = float(input("Informe o  valor do salario fixo: "))
comissao_produto = float(input("informe o valor da comissao por produto: "))
quantidade_produtos = float(input("Informe a quantidade de produtos vendidos: "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

print(f"O salario total do vendedor será: {salario_total}")