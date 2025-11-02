
dia = int(input("Insira o numero do dias: "))
producao_total = 0
dias_acima_meta = 0
bonus = 0

for n in range(1,dia + 1):
    producao_dia = int(input(f"Insira a produção do dia {n}: "))
    meta_diaria = 50
    producao_total += producao_dia
    if producao_dia >= meta_diaria:
        dias_acima_meta += 1

meta_diaria = producao_total / dia

if meta_diaria > 60 and dias_acima_meta >= 4:
    print("BÔNUS MÁXIMO! (15% sobre a produção total).")
    bonus =producao_total * 0.15
elif meta_diaria >  50 or dias_acima_meta >= 3:
    print("BÔNUS PARCIAL! (5% sobre a produção total).")
    bonus =producao_total * 0.05
else:
    print("Sem Bônus. Metas de produtividade não foram atingidas.")
    
print(f"Média Diária de Produção: {meta_diaria:.2f} unidades")
print(f"Valor Final do Bônus: R$ {bonus:.2f}")
