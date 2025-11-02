TOLERANCIA = 0.5
TAMANHO_IDEAL = 15.0

numero_total_de_pecas = int(input("Digite o número total de peças a serem inspecionadas: "))

soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0
contador = 1

while contador <= numero_total_de_pecas:
    tamanho_medido = float(input(f"Tamanho medido da peça {contador} (em cm): "))
    soma_dos_tamanhos += tamanho_medido
    desvio = abs(tamanho_medido - TAMANHO_IDEAL)
    if desvio > TOLERANCIA:
        pecas_fora_tolerancia += 1
    contador += 1

media_tamanho = soma_dos_tamanhos / numero_total_de_pecas

print("\nResultado da Inspeção:")
if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")

print(f"Média de Tamanho das Peças: {media_tamanho:.2f} cm")
print(f"Quantidade de Peças Fora da Tolerância: {pecas_fora_tolerancia}")