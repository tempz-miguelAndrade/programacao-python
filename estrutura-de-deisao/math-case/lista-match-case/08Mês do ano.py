#    Leia um número de 1 a 12 e exiba o nome do mês.

mes = input("Informe o mês(Pode ser em número também): ").lower()

match mes:
    case _ if mes == "1" or mes == "2" or mes == "12" or mes == "janeiro" or mes == "fevereiro" or mes == "dezembro":
        print("Verão!")
    case _ if mes == "3" or mes == "4" or mes == "5" or mes == "março" or mes == "abril" or mes == "maio":
        print("Outono!")
    case _ if mes == "6" or mes == "7" or mes == "8" or mes == "junho" or mes == "julho" or mes == "agosto":
        print("Inverno!")
    case _ if mes == "9" or mes == "10" or mes == "11" or mes == "setembro" or mes == "outrubro" or mes == "novembro":
        print("Primavera!")
    case _:
        print("Mês inválido!")