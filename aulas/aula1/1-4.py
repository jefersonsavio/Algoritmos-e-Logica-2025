preco = int(input("Digite o preço: "))
desconto_percent = int(input("Digite o desconto: "))
desconto = preco*(desconto_percent/100)
preco_final = preco-desconto

print(f"O preco com desconto é: {preco_final}")   