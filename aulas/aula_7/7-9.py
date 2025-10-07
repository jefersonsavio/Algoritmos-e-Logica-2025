plano = input("Qual o seu plano :'premium', 'padrão' ou 'básico' ")
meses = int(input("Há quantos meses voça ja é assinante? "))
conta = input("Sua conta é compartilhada? 'sim' ou 'não' ")

if plano == "premium" and meses >= 24:
    print("Você é um cliente premium de longa data: 25% de desconto vitalício!")
elif plano == "padrão" and meses > 12 and conta == "não":
    print("Você atende aos critérios para um desconto de 15%.")
elif plano =="básico" and meses > 6:
    print("Sua lealdade merece um reconhecimento: 5% de desconto na próxima fatura.")
else:
        print("Nenhum desconto disponível no momento para o seu perfil.")

