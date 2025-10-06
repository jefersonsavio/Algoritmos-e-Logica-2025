
plano = input("Informe qual seu plano:'basico', 'padrão' ou 'premium': ")
uso = int(input("Unforme quantos meses voçe já e assinante desse plano: "))

if plano == 'padrão' or 'premium':
    if uso >= 12 and uso <= 24:
        print("Parabéns! Você tem direito a um desconto de 15%.")
    else:
        print("Seu plano é elegível, mas você não atende ao tempo de uso necessário para o desconto.")

else:
    print("Seu plano não é elegível para este desconto.")