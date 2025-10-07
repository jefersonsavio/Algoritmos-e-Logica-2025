
distancia = float(input("Digite a distancia em quilometros a ser percorrida: "))
velocidade = float(input("Digite a velocidade em km/h da viagem: "))

tempo = distancia / velocidade


if tempo > 4:
  print("viagem demorada, utilizar veículo sedan")
else:
  print("viagem rápida, utilizar veículo hatch")
