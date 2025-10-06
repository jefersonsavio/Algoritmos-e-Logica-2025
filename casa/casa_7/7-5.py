
#A estrutura if/elif/else é um recurso de programação para a tomada de decisões
#executando um bloco de código apenas se a condição for verdadeira ou outro se a primeira for falsa.
#O if inicia o bloco, o elif (else if) verifica uma condição alternativa caso o if seja falso
#e o else é executado se todas as condições anteriores falharem

# Dando valor pra variável
idade = int(input("Informe a idade: "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade.")
# Se a primeira condição (if) for falsa, verifica se a idade é maior ou igual a 16
elif idade >= 16:
    print("Você é adolescente!")
# Se nenhuma das condições anteriores for verdadeira, executa o bloco else
else:
    print("Você é menor de idade!")
