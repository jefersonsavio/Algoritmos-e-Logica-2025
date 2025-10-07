valor = float(input("Informe o valor da compra: "))

if valor >  100:
    valor = valor-(valor*0.05)
    if valor > 150:
        valor = valor-(valor*0.02)
        print(f"Valor da compra com super desconto: {valor}")
    else:
     print(f"valor com desconto: {valor}")
else:
    print("sem desconto")