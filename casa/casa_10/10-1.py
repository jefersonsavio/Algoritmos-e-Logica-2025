quantidade_notas = int(input("Quantas notas fiscais? "))
soma_das_notas = 0.0
for n in range(quantidade_notas):
    valor_nota = float(input(f"Digite o valor da nota fiscal {n + 1}: R$ "))
    soma_das_notas += valor_nota
    if soma_das_notas <  1000.00:
        aliquota = 0.05
    elif soma_das_notas >= 1000.00 and soma_das_notas < 5000.00:
        aliquota = 0.09
    elif soma_das_notas >= 5000.00 and soma_das_notas < 15000.00:
        aliquota = 0.12
    else:
        aliquota = 0.16
        
    valor_imposto = soma_das_notas * aliquota

    print(f"")
        
        
print(f"Valor total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota * 100:.0f}%")
print(f"Valor do imposto a ser pago: R$ {valor_imposto:.2f}")
