#-------------------------
# EXPLIQUE O QUE FAZ ESSE PROGRAMA
# calcula o custo total do envio

# EXPLIQUE OS IF/ELSE ANINHADOS
#calcula o preço da entrega do produto ao seu destino de acordo com seu peso

peso = float(input("Digite o peso do pacote em kg: ")) # atribui um valor à variável "peso"
destino = input("Digite o destino ('local' ou 'nacional'): ").lower() # atribui um valor à variável "destino" 

custo_total = 0.0 # atrbui valor "0" à variável "custo_total"

if destino == 'local': # se o destino for 'local', entra nesse bloco
    custo_base = 5.00 # atribui valor '5' a variável "custo_base"
    if peso > 10: # se a variável peso for maior que '10' entra nesse bloco
        excesso_peso = peso - 10
        custo_extra = excesso_peso * 2.00
        custo_total = custo_base + custo_extra
    else: # se a variavel peso não for maior que '10' entra nesse bloco
        custo_total = custo_base
    print(f"O custo total do envio para o destino local é: R$ {custo_total:.2f}")

else:  # Se o destino não for 'local', entra neste bloco
    if destino == 'nacional': # se o destino for 'nacional' entra nesse bloco
        custo_base = 15.00
        if peso > 10:  # se a variável peso for maior que '10' entra nesse bloco
            excesso_peso = peso - 10
            custo_extra = excesso_peso * 5.00
            custo_total = custo_base + custo_extra
        else:
            custo_total = custo_base
        print(f"O custo total do envio para o destino nacional é: R$ {custo_total:.2f}")
    else: # se o destino não for 'nacional' entra nesse bloco
        print("Erro: Destino inválido. Por favor, digite 'local' ou 'nacional'.")