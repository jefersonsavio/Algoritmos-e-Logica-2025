simbol = input("Digite algum símbolo (ex: #, *, @): ")

quantidade = int(input("Digite a quantidade de vezes que voce quer repetir o simbolo: "))

print("\n----- Padrão Gerado -----")

for i in range(quantidade):
  print(simbol)

print("-------------------------------")