a = float(input("Dê um valor a A: "))
b = float(input("Dê um valor a B: "))
c = float(input("Dê um valor a C: "))
d = float(input("Dê um valor a D: "))
e = float(input("Dê um valor a E: "))
f = float(input("Dê um valor a F: "))

x = ((c*e)-(b*f))/((a*e)-(b*d))
y = ((a*f)-(c*d))/((a*e)-(b*d))

print(f"O valor de x é: {x}")
print(f"O valor de y é: {y}")