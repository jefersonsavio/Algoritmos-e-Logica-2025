V_base = float(input("Digite o Valor Base do Bônus: "))
P_ind = float(input("Digite a Pontuação de Performance Individual de 0 a 100: "))
P_equipe = float(input("Digite a Pontuação de Meta da Equipe de 0 a 100: "))

if P_ind > 90:
    FAP = 1.25
elif P_ind > 70:
    FAP = 1.10
elif P_ind > 50:
    FAP = 1.00
else:
    FAP = 0.80

B_ajustado = V_base * FAP

if P_equipe > 85:
    if P_ind > 95 or B_ajustado > 5000:
        print("Bônus Máximo de 30% extra.")
        B_final = B_ajustado * 1.30
    else:
        print("Bônus Padrão de 10% extra.")
        B_final = B_ajustado * 1.10
elif P_equipe >= 60:
    if P_ind < 60:
        print("Penalidade por Desempenho Individual (15% de Redução).")
        B_final = B_ajustado * 0.85
    else:
        print("Sem Alteração Adicional.")
        B_final = B_ajustado
else:
    print("Penalidade Severa (25% de Redução).")
    B_final = B_ajustado * 0.75

print(f"Valor Base do Bônus: R$ {V_base:.2f}")
print(f"Fator de Ajuste Aplicado (FAP): {FAP}")
print(f"Bônus Final: R$ {B_final:.2f}")