from os import stat


total = float(input("Informe o valor total da compra: "))
status = input("Voçe é cliente 'novo' ou 'fiel'? ")
produto = input("Voçe procura por produto 'eletronico' ou 'livro'? ")

if total >= 200 and status == "fiel":
    print("Parabéns! Você tem direito a frete grátis e um brinde especial.")
elif total >= 200 or produto == "livro":
    print("Você tem direito a frete grátis. Aproveite!")
elif status == "fiel" and produto == "eletronico":
    print("Você tem direito a um desconto de 5% no frete.")
else:
    print("Não há promoções aplicáveis a este pedido.")
