#part 1
num_lotes = int(input("Digite o número de lotes de produção a serem simulados: "))
custo_fixo = 0.0
lista_custos_por_lote = []

for i in range(num_lotes):
    unidades = int(input(f"Digite o número de unidades produzidas no lote {i+1}: "))

    if unidades > 50:
        C_var_unidade = 1.50
    elif  unidades <=20 and unidades <= 50:
        C_var_unidade = 2.00
    else:
        C_var_unidade = 3.00

    custo_lote = custo_fixo + (unidades * C_var_unidade)

    lista_custos_por_lote.append(custo_lote)
    
#part 2

preco_base_venda = 5.00
lucro_total_acumulado = 0.0
lotes_com_lucro_alto = 0

for i in range(len(lista_custos_por_lote)):
    custo_lote = lista_custos_por_lote[i]
    receita = 50 * preco_base_venda
    lucro = receita - custo_lote
    lucro_total_acumulado += lucro

    if lucro > 100.00:
        lotes_com_lucro_alto += 1
        print(f"Lote {i+1} Aprovado: Lucro Alto.")
    elif lucro > 0.00:
        print(f"Lote {i+1} Aceitável: Lucro Mínimo.")
    else:
        print(f"Lote {i+1} Reprovado: Prejuízo.")

print(f"Lucro Total Acumulado: R$ {lucro_total_acumulado:.2f}")
print(f"Quantidade de Lotes com Lucro Alto: {lotes_com_lucro_alto}")