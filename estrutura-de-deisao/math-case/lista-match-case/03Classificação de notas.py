#   Leia uma nota de 0 a 10 e exiba:
#   * `A` (8–10)
#   * `B` (6–7.9)
#   * `C` (4–5.9)
#   * `D` (0–3.9)

nota = float(input("Informe sua nota: "))

match nota:
    case _ if nota >= 8 and nota <= 10:
        print("A")
    case _ if nota >= 6 and nota <= 7.9:
        print("B")
    case _ if nota >= 4 and nota <= 5.9:
        print("C")
    case _ if nota >= 0 and nota <= 3.9:
        print("D")
    case _:
        print("Informação inválida!")