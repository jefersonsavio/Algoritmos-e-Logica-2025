print("Calculando a hipotenusa do triangulo")

cateto_1 = float(input("Informe o valor do primeiro cateto: "))
cateto_2 = float(input("Informe o valor do segundo cateto: "))

hipotenusa = (cateto_1**2 + cateto_2**2)**0.5

print(f"O valor da hipotenusa é: {hipotenusa}")

if hipotenusa > 180:
    print("O triangulo deve ser refeito para ser compativel com proposta")
else: 
    print("Triangulo incluso na proposta")