from pydoc import cli


tamanho = input("Escolha o tamanho da pizza: 'pequena', 'média' ou 'grande' ")
sabor = int(input("Quantos sabores deseja? "))
cliente = input("Voçe é cliente 'vip ou 'normal?' ")

if tamanho == "grande" and sabor > 2:
    print("Pedido especial: sujeito a taxa extra.")
elif tamanho == "grande" or cliente == "vip":
    print("Pedido prioritário: prepare para entrega rápida.")
elif tamanho == "média" and sabor <= 1:
    print("Pedido padrão: processamento normal.")
else:
    print( "Pedido de baixo volume: pode ser processado a qualquer momento.")
