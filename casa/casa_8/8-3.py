import math

ladoA = int(input("Informe lado A do triangulo: "))
ladoB = int(input("Informe lado B do triangulo: "))
ladoC = int(input("Informe lado C do triangulo: "))

coseno = (ladoA**2 + ladoB**2 - ladoC**2) / (2 * ladoA * ladoB)
angulo = math.degrees(math.acos(coseno))

if  angulo == 90 :
    print("triangulo retangulo")
elif angulo < 90 :
    print("triangulo acutangulo")
elif angulo> 90 :
    print("Triangulo obtusangulo")
else:
    print("Não é um triangulo")
