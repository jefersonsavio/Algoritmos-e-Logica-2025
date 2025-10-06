
clima = input("Como está o tempo? 'limpo', 'nublado' ou 'tempestade' ")
visibilidade = int(input("Em quantos metros está a visibilidade?: "))
motor = input("Informe o status do motor: 'ok' ou 'avaria'")

if clima == "limpo" and visibilidade > 1000:
    print("Condições de decolagem ideais. Autorizado.")
elif clima == "nublado" and visibilidade >= 500 and motor == "ok":
    print("Condições de decolagem aceitáveis. Aguardando autorização final.")
elif motor== "avaria":
    print("Decolagem negada. Avaria no motor detectada.")
else:
    print("Condições de segurança não atendidas. Voo atrasado.")
