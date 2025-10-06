print("Calculando o perimetro do terreno")

frente =  float(input("Dê a metragem da frente do terreno: "))
fundo = float(input("Dê a metragem do fundo do terreno: "))

perimetro = 2 * (frente + fundo)

print(f"O perimetro do terreno é: {perimetro}")

if perimetro >16:
    print("Alteração de cadastro aprovada")
else:
    print("Alteração de cadastro reprovada")