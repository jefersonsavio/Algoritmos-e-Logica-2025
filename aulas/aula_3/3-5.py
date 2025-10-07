import math

print("Vamos implementar as coordenadas do ponto cartesiano")

x1 = int(input("Dê valor ao ponto x1: "))
x2 = int(input("Dê valor ao ponto x2: "))
y1 = int(input("Dê valor ao ponto y1: "))
y2 = int(input("Dê valor ao ponto y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distancia entre os dois pontos é: {distancia}")