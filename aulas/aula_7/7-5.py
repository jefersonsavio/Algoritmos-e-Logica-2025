from tokenize import Double


media = float(input("digite a média do aluno: "))
habilidade = int(input("Digite seu nível de habilidadenuma escala de 1 a 5: "))
status = input("Voçe possui dificuldade financeira? 'sim' ou 'não': ")

if media >= 9.0 and habilidade >=4:
    print("Parabéns! Você é elegível para a bolsa de mérito acadêmico.")
elif media >= 8.0 and status == "sim":
    print("Parabéns! Você é elegível para a bolsa de necessidade financeira.")
elif media >= 7.0 and habilidade >= 3 and status =="sim":
    print("Parabéns! Você é elegível para a bolsa combinada de mérito e necessidade.")
elif media>= 7.0 and habilidade > 3:
    print("Você é elegível para a bolsa de necessidade, mas sua média e habilidade em escrita são requisitos.")
else: 
    print("Infelizmente, você não atende aos critérios de elegibilidade para bolsa.")
