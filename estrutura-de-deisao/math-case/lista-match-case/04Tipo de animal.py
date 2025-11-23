#   Leia o nome de um animal e classifique:
#   * "cachorro" ou "gato" → **Mamífero**
#   * "cobra" ou "lagarto" → **Réptil**
#   * "sapo" → **Anfíbio**
#     Se não estiver na lista, exibir **"Animal não identificado"**.

nome= input("Informe o nome do animal('chacorro' ou 'gato' = Mamífero): ").lower()

match nome:
    case _ if nome == "cachorro" or nome == "gato":
        print("Mamífero")
    case _ if nome == "cobra" or nome == "lagarto":
        print("Réptil")
    case _ if nome == "sapo":
        print("Anfíbio")
    case _:
        print("Animal não identificado!")