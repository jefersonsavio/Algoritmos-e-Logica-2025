dias = int(input("Insira o numero de dia ser analizados: "))
soma_temperaturas = 0.0

for n in range(dias):
    graus = float(input(f"Informe a temperatura em graus celsius do dia {n+1}: "))
    soma_temperaturas += graus
    
media = soma_temperaturas / dias

if media > 28:
     print("Média de temperatura: Clima Quente.")
elif media <= 28 and media >=18:
    print("Média de temperatura: Clima Agradável.")
else:
    print("Média de temperatura: Clima Frio.")

print(f"A media de temperatura foi: {media:.2f} graus celsius!")