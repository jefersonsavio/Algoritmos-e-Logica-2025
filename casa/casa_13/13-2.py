numero_total_de_pecas = int(input("Digite o número total de peças no lote: "))

CUSTO_FIXO_INSPECAO = 150.00
CUSTO_RETRABALHO = 25.00

erros_criticos = 0
erros_leves = 0
custo_variavel_rejeicao = 0.0

for n in range(numero_total_de_pecas):
    nivel_defeito = int(input(f"Digite o nível de defeito da peça {n+1} (0 a 10): "))

    if nivel_defeito > 8:
        erros_criticos += 1
        custo_variavel_rejeicao += CUSTO_RETRABALHO
    elif 3 <= nivel_defeito <= 8:
        erros_leves += 1
    else:
        print("Peça Aprovada.")

taxa_rejeicao = (erros_criticos / numero_total_de_pecas) * 100
custo_final = CUSTO_FIXO_INSPECAO + custo_variavel_rejeicao

print("\nResultado da Inspeção:")
if taxa_rejeicao > 10 and erros_leves > 5:
    classificacao = "LOTE REPROVADO! Alta taxa de defeito e muitos erros leves."
elif erros_criticos > 2 or taxa_rejeicao > 20:
    classificacao = "LOTE CRÍTICO! Necessário reavaliação total."
else:
    classificacao = "LOTE APROVADO! Custos sob controle."

print(f"Taxa de Rejeição: {taxa_rejeicao:.2f}%")
print(f"Custo Final da Inspeção: R$ {custo_final:.2f}")
print(classificacao)