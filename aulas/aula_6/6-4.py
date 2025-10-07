idade = int(input("Informe sua idade: "))
nacionalidade = input("Diga se voçe é 'estrangeiro' ou 'brasileiro': ")

if idade >= 60:
    if nacionalidade == "brasileiro":
        print("Voçe tem um desconto especial:", nacionalidade)
    else:
        print("voçe tem direito a desconto padrão")

else:
    print("Voce não tem direito a desconto")