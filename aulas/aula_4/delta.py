from cmath import sqrt
import math

a = int(input("De o valor de A: "))
b = int(input("De o valor de B: "))
c = int(input("De o valor de C: "))

delta = b*b - 4 * a * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:

    print(f"A equação possui uma raiz real: x = ")
else:

    print(f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}")


print(f"O Valor de x1 é: {x1}")
print(f"O Valor de x é: {x2}")
