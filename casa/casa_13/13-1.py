num_vendedores = int(input("Digite o número total de vendedores a serem avaliados: "))

valor_base_bonus = 500.00

pontuacao_total_equipe = 0.0
vendedores_acima_meta = 0
botao_alerta_ativados = 0

for i in range(1, num_vendedores + 1):
    pontuacao = int(input(f"Pontuação Final de Vendas do vendedor {i} (0 a 100): "))
    pontuacao_total_equipe += pontuacao

    if pontuacao >= 90:
        vendedores_acima_meta += 1
    elif pontuacao < 50:
        botao_alerta_ativados += 1

media_equipe = pontuacao_total_equipe / num_vendedores
bonus_base_total = num_vendedores * valor_base_bonus

if media_equipe > 80 and botao_alerta_ativados == 0:
    FMB = 1.20
elif vendedores_acima_meta > (num_vendedores / 2) or (70 <= media_equipe <= 80):
    FMB = 1.05
elif botao_alerta_ativados > 1:
    FMB = 0.80
else:
    FMB = 1.00

valor_final_total = bonus_base_total * FMB

print(f"Média de Pontuação da Equipe: {media_equipe:.2f}")
print(f"Número de Alertas Ativados: {botao_alerta_ativados}")
print(f"Valor Final Total a Pagar: R$ {valor_final_total:.2f}")