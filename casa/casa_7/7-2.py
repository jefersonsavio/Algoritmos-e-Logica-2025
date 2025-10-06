idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
saude = input("Informe se sua saúde está 'boa' ou'ruim': ")

if idade>18 and peso >= 50:
    if saude == 'boa':
        print("Você está elegível para doar sangue!")
    else: 
        print("Você não pode doar sangue devido à sua condição de saúde.")
else:
    print("Você não está elegível para doar sangue. Verifique os requisitos de idade e peso.")

