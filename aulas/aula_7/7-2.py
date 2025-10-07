idade = int(input("Informe a idade: "))
genero = input("Informe o generodo filme: 'terror' ou 'ação' ")

if idade < 18 and genero =="terror":
    print("Este filme não é recomendado para sua idade devido ao gênero.")
elif idade < 16 and genero == "ação":
    print("Este filme de ação não é adequado para sua faixa etária.")
elif idade >= 18 or genero =="ação":
    print("Recomendado para você: assistir o filme.")
else:
    print("Não há recomendações para este filme ou idade.")
