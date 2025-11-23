#    Leia um número de 1 a 7 e use `match` para exibir o dia correspondente (1 = Domingo, 2 = Segunda...).

dia = int(input("Informe o dia em números(1 = Domingo, 2 = Segunda...): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Informação inválida!")
