#    Leia um código de usuário:
#    * `1` → Administrador
#    * `2` → Usuário comum
#    * `3` → Visitante
#      Caso contrário, exibir **Código inválido**.

codigo = int(input("Informe o seu código: "))

match codigo:
    case 1:
        print("Administrador")
    case 2:
        print("Usuário comum")
    case 3:
        print("Visitante")
    case _:
        print("Código inválido!")