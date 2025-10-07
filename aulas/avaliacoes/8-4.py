# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! Zé DA MANGA!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

P = float(input("Informe o valor inicial do investimento: "))
T = int(input("Informe o prazo do investimento em meses: "))

if T < 6 :
    j = 0.005
    print("Taxa de juros mensal aplicada em 5%")
elif T > 6 and T < 12:
    j = 0.008
    print("Taxa de juros mensal aplicada em 8%")
elif T >12:
    j = 0.012
    print("Taxa de juros mensal aplicada em 12%")

print(f"O rendimento foi de: R$: {P*j*T}")
print(f"O valor do investimento final é: R$: {(P*j*T) + P:.2f}")



