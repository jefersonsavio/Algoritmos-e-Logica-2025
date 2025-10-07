# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! Zé DA MANGA!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

R_investimento = float(input("Informe o retorno do investimento: "))
R_livre = float(input(" Informe a taxa livre de risco: "))
Sigma = float(input("Informe o desvio-padrão da volatilidade: "))

Sharp = (R_investimento - R_livre) / Sigma
Spread = R_investimento - R_livre

if Sharp > 1.5 and Spread > 0.05:
     print("Investimento Excelente: Alta performance ajustada ao risco")
elif Sharp > 0.5 and Sharp <= 1.5 or Spread >0.02:
    print("Investimento Bom: Risco e retorno moderados")
elif Sharp < 0.5 and R_investimento > 0:
    print("Investimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
else: 
    print("Investimento Ruim: Não recomendado.")

print(f"Valor do Sharp ratio: {Sharp}")

