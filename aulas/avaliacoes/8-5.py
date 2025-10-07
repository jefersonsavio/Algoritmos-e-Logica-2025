# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! Estamos indo!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

c_inicial = float(input("Informe o custo inicial do produto: "))
Q = int(input("Informe a quantidade de produtos produzidos: "))
Dias = int(input("Informe quantos dia de atraso: "))
Defeito = float(input("Informe o percentual de defeito do produto: "))


if Q > 100 and c_inicial > 1000:
    Fator_comp = 1.15
else:
    Fator_comp = 1.05

Custo_corrigido = c_inicial *Fator_comp
Custo_final = Custo_corrigido * 1.25 

if Defeito > 0.10 or Dias > 5:
    print("Penalidade Alta: 20% De redução no lucro.")
    Custo_final = Custo_corrigido * 1.25
    print(f"O custo final dp produto é: {Custo_final}")
elif Defeito > 0.05 and Defeito <= 0.10 or Dias > 0:
    print("Penalidade Média: 10% De redução no lucro.") 
    Custo_final = Custo_corrigido * 1.10
    print(f"O custo final dp produto é: {Custo_final}")
else:
    print("Sem penalidade. Custo final apenas com correção.")
    Custo_final = Custo_corrigido
    print(f"O custo final dp produto é: {Custo_final}")