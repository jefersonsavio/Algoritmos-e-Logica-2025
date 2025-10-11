# Jeferson Cristiano Sávio
# R.A 0220482523029
# Diga olá para o fatecando mais dedicado! Bora!
print("Jeferson Cristiano Sávio, R.A 0220482523029")

glicose = float(input("Insira seu nivel de glicemia em jejum: "))
print (f"glicose em: {glicose} mg/dL ")

if glicose < 100 :
    print("Glicemia Normal.")
elif glicose > 100 and glicose < 125:
    print("Pré-diabetes: Risco Moderado.")
else: print("Diabetes: Nível Alto.")

