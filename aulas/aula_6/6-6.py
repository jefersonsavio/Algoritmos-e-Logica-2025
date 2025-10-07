temperatura = int(input("Informa quantos graus celsius está la fora: "))
chuva = input("está chovendo (digite 'sim' ou 'não'): ")

if temperatura > 20 and chuva == 'não':
    print("O tempó está ideal para atividade ao ar livre!")
    if temperatura >= 15 and temperatura <= 20 or chuva == 'sim':
        print(" O tempo não está ideal para atividade ao ar livre")
else:
    print("O tempo não está propicio a atividades ao ar livre!")




