#   Pergunte a última letra da placa e exiba:
#   * `A` ou `B` → **Rodízio segunda**
#   * `C` ou `D` → **Rodízio terça**
#   * `E` ou `F` → **Rodízio quarta**
#   * etc.

letra = input("Informe a última letra da placa: ").lower()

match letra:
    case _ if letra == "a" or letra == "b":
        print("Rodízio segunda")
    case _ if letra == "c" or letra == "d":
        print("rodízio terça")
    case _ if letra == "e" or letra == "f":
        print("Rodízio quarta")
    case _:
        print("Rodízio não encontrado!")