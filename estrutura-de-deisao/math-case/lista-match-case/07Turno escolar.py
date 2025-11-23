#   Leia `M`, `V` ou `N` e exiba:
#   * `M` → **Matutino**
#   * `V` → **Vespertino**
#   * `N` → **Noturno**
#     Caso contrário, informar **inválido**.

letra = input("Informe uma letra('M' Matutino, 'V' Vespertino e 'N' Noturno): ").lower()

match letra:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa noite!")
    case _:
        print("Informação inválida!")