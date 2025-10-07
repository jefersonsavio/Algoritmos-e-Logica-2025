vendas = int(input("Qual o valor de vendas no mes? "))
satisfacao = float(input("Em uma escala de 0.0 a 1.0 Qual seu nivel de satisfação? "))
meta = input("A meta de novos clientes foi atingida? 'sim' ou 'não' ")

if vendas >= 50000 and satisfacao > 0.9:
    print("Vendedor de alta performance: classificado como Sênior.")
elif vendas >= 30000 and meta == "sim":
    print("Vendedor de bom desempenho: classificado como Pleno.")
elif satisfacao > 0.8 or meta == "sim":
    print("Vendedor em desenvolvimento: classificado como Júnior.")
else:
    print("Vendedor em revisão de desempenho: não atende aos critérios mínimos.")
