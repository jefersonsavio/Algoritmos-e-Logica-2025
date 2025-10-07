print("Calculando salario mensal")

salario_bruto = float(input("Informe o seu salario: "))
horas_extras = int(input("Informe a quantidade de horas: "))

descontos = salario_bruto * 0.08
imposto = salario_bruto * 0.15
salario = salario_bruto - descontos + (horas_extras * 50.0) - imposto

print(f"O seu salario do mes com desconto  e horas extras deu: {salario}")