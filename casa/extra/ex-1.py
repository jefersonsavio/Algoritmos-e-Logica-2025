salario = float(input("Informe o salario: "))
horas = int (input("Informe o total de hoas trabalhadas"))


if salario > 5000 and horas < 40:
    adicional=0.15
else:
   adicional=0.18


print(f"O salario final é: {salario+adicional}")