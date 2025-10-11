numero = int(input("Insira um nomer de 1 a 9"))

print(f"\n--- Tabuada do {numero} ---")

for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

print("--------------------------")