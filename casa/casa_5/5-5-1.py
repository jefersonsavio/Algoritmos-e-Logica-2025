import math

print("Plano cartesiano")

x1 = float(input("Dê o valor de x1: "))
x2 = float(input("Dê o valor de x2: "))
y1 = float(input("Dê o valor de x1: "))
y2 = float(input("Dê o valor de x1: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"a distancia entre os ponto é: {distancia}")

