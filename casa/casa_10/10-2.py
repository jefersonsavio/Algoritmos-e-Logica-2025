quantidade_dias = int(input("Digite a quantidade de dias a serem analisados: "))

vendas_totais = 0.0

for n in range(quantidade_dias):
    valor_venda = float(input(f"Digite o valor da venda do dia {n + 1}: R$ "))
    vendas_totais += valor_venda

media_diaria = vendas_totais / quantidade_dias

if media_diaria > 1500.00:
    imposto_fixo = 200.00
else:
    imposto_fixo = 50.00

if vendas_totais > 10000.00:
    taxa_percentual = 0.08
else:
    taxa_percentual = 0.05

valor_taxa_servico = vendas_totais * taxa_percentual

valor_liquido_final = vendas_totais - valor_taxa_servico - imposto_fixo

print(f"Valor total das vendas: R$ {vendas_totais:.2f}")
print(f"Imposto Fixo aplicado: R$ {imposto_fixo:.2f}")
print(f"Taxa de Serviço aplicada: {taxa_percentual * 100:.0f}%")
print(f"Valor líquido final da empresa: R$ {valor_liquido_final:.2f}")