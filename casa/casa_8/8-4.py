P = float(input("Digite o valor do empréstimo: R$ "))
J_anual = float(input("Digite a taxa de juros anual em %: "))
N = int(input("Digite o prazo do empréstimo em meses: "))

J_mensal = (J_anual / 12) / 100
pagamento_mensal = P * (J_mensal * (1 + J_mensal)**N) / ((1 + J_mensal)**N - 1)
print(f"Pagamento mensal: R$ {pagamento_mensal:.2f}")

# Classifica o pagamento mensal
if pagamento_mensal < 200:
    print("Pagamento mensal baixo")
elif 200 <= pagamento_mensal <= 500:
    print("Pagamento mensal moderado")
else:
    print("Pagamento mensal alto")
