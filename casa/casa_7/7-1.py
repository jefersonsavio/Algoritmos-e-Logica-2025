idade = int(input("Informe sua idade: "))
xp = int(input("Informe quantos anos de experiencia voçe tem: "))
disponibilidade = input("Informe se voçe tem disponibilidade de 'manhã' ou de 'tarde': ")

if idade > 18 and xp > 1:
    if disponibilidade == 'manhã' or disponibilidade == 'tarde':
        print("Parabéns! Voçe é elegível à vaga.")
    else:
        print("Não elegível: Disponibilidade não corresponde aos requisitos.")
else:
    print("Não elegível: Idade ou experiência insuficientes.")