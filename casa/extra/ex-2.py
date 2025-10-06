numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


if numero1 % numero2 == 0 and numero2 % numero1 == 0:
    
    print("Os números são divisíveis entre si")
else:
    
    print("Os números não são divisíveis entre si")