total_lancamentos = int(input("Digite o número total de lançamentos financeiros: "))

saldo_final = 0.0
total_receitas = 0.0
total_despesas = 0.0

for i in range(1, total_lancamentos + 1):
    valor = float(input(f"Valor da Transação {i} : "))
    
    if valor > 0:
        total_receitas += valor
    else:
        total_despesas += abs(valor)
    
    saldo_final += valor

# Avaliação final e aplicação de taxa ou bônus
if saldo_final > 0 and total_receitas > (total_despesas * 2):
    print("\nSituação Excelente: Bônus de 5% sobre o saldo aplicado.")
    saldo_ajustado = saldo_final * 1.05
elif saldo_final > 0:
    print("\nSituação Boa: Sem bônus ou taxa.")
    saldo_ajustado = saldo_final
else:
    print("\nSituação Ruim: Taxa de serviço de 2% aplicada.")
    saldo_ajustado = saldo_final * 0.98

print(f"Total de Receitas: R$ {total_receitas:.2f}")
print(f"Total de Despesas: R$ {total_despesas:.2f}")
print(f"Saldo Final Ajustado: R$ {saldo_ajustado:.2f}")