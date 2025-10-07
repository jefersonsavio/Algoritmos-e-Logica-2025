salario = float(input("Informe o salario: "))

if salario < 5000:
    imposto=salario*0.18
else:
    imposto=salario*0.27

print(f"O imposto sobre o salario será de: {imposto:.2f}")