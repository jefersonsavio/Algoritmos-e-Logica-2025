senha_certa = "654321"
usuario_certo = "alukard@empresa.com"

u = input("Informe username: ")

if u == usuario_certo:
    p = input("Informe password: ")
    if p == senha_certa:
        print("credenciais válidas")
    else:
        print("senha inválida!")
else:
    print("usuario inválido")        
