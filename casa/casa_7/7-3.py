
orcamento = float(input("Informe o orçamento solicitado: "))
membros = int(input("Informe quantos membros fazem parte da equipe: "))
area_pesq = input("informe se a área de atuação é de 'inovação' ou 'sustentabilidade': ")

if orcamento > 50000 and membros >= 3:
    if area_pesq == "sustentabilidade" or "invação":
        print("Projeto qualificado para o financiamento!")
    else:
        print("Projeto não qualificado: A área de pesquisa não é prioritária.")
else:
    print( "Projeto não qualificado: Orçamento ou tamanho da equipe insuficientes.")