print("Informe sua idade em anos,meses e dias")

anos = int(input("Quantos anos: "))
meses = int(input("Quantos meses: "))
dias = int(input("quantos dias: "))

dias_anos = anos * 365
dias_meses = meses * 30
total_dias = dias_anos + dias_meses + dias

print(f"O total de dias da sua idade é: {total_dias}")