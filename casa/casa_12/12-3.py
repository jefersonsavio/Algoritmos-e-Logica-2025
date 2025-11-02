total_prod = int(input("Digite o número total de produtos a serem analisados: "))

total_estoque = 0.0
prod_alto_risco = 0

for i in range(1, total_prod + 1):
    print(f"\nProduto {i}:")
    preco_unitario = float(input("Preço Unitário (R$): "))
    quantidade_estoque = int(input("Quantidade em Estoque: "))

    valor_bruto = preco_unitario * quantidade_estoque

    if quantidade_estoque > 100:
        total_estoque += valor_bruto * 1.05
    elif preco_unitario > 50.00 and quantidade_estoque <= 10:
        prod_alto_risco += 1
        total_estoque += valor_bruto
    else:
        total_estoque += valor_bruto

print(f"Valor Total do Estoque: R$ {total_estoque:.2f}")
print(f"Número de Produtos Classificados como Alto Risco: {prod_alto_risco}")