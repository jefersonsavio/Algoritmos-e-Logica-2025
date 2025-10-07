xp = int(input("Quantos anos  de experiencia voçe tem? "))
habilidade = int(input("Defina sua habilidade de comunicação de 1 a 10: "))
disponivel = input(
    "Qual sua diponibilidade de horario? 'integral' ou 'meio-período' ")

if xp > 2 and habilidade > 8:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga integral.")
elif xp > 2 and habilidade > 6:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga de meio período.")
elif xp > 1 and habilidade > 8 and disponivel == "meio-período":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga de meio período.")
elif xp > 1 and habilidade > 8 and disponivel == "integral":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga integral.")
elif habilidade > 7 and disponivel == "meio-período":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga de meio período.")
elif habilidade > 7 and disponivel == "integral":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga integral.")
else:
    print("Candidato não classificado. Não atende aos requisitos mínimos.")
