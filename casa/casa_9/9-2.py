# O for é uma estrutura de repetição usada para iterar sobre elementos de uma sequência
# como listas, tuplas(estrutura de dados que permite armazenar vários valores em uma única variável)
# strings ou até mesmo intervalos numéricos.
# Ele executa um bloco de código para cada item da sequência.


numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
