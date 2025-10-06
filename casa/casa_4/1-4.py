
capital = float(input("Insira a capital da empresa: "))
taxa_juros  = float(input("Insira a ataxa de juros da empresa: "))
tempo  = int(input("Insira o tempo de aplicação: "))

juros = capital * taxa_juros * tempo

valor_total = capital + juros

print(f" valor dos juros: {juros}")
print(f"O valor total: {valor_total}")