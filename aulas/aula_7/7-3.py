ingresso = input("Informe o tipo de ingresso: 'padrão' ou 'premium' ")
idade = int(input("Informe sua idade: "))
lista = input("voçe tem convite VIP? 'sim' ou 'não' ")


if ingresso == "premium":
    print("Acesso total: todas as áreas e benefícios especiais.")
elif idade >= 18 and lista == "sim":
    print("Acesso VIP: área exclusiva e entrada prioritária.")
elif idade >= 18 or lista == "padrão":
    print("Acesso padrão: entrada para a área principal do evento.")
else: print("Acesso negado: verifique os critérios de entrada.")


