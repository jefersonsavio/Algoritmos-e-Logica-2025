quantidade_dias = int(input("Digite a quantidade de dias a serem analisados: "))

soma_das_temperaturas = 0.0

for i in range(quantidade_dias):
    temperatura = float(input(f"Digite a temperatura do dia {i + 1} (°C): "))
    soma_das_temperaturas += temperatura

media_temperatura = soma_das_temperaturas / quantidade_dias

if media_temperatura > 28.0:
    classificacao = "Clima Quente"
elif 18.0 <= media_temperatura <= 28.0:
    classificacao = "Clima Agradável"
else:
    classificacao = "Clima Frio"

print("-------------------------------")
print(f"Média de temperatura: {media_temperatura:.2f}°C")
print(f"Classificação: {classificacao}")