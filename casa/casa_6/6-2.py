custoFabrica = float(input("Digite o custo de fábrica do carro: "))

porcentDistribuidor = float(input("Digite a porcentagem do distribuidor (ex: 28 para 28%): "))

valorImpostos = float(input("Digite o valor dos impostos: "))

custoFinal = custoFabrica + (custoFabrica * porcentDistribuidor / 100) + valorImpostos

print(f"O custo final ao consumidor é: R$ {custoFinal:.2f}")