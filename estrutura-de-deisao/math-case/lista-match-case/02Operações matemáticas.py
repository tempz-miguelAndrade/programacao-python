#    Leia dois números e uma operação (`+`, `-`, `*`, `/`) e use `match` para executar a operação correta.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
operador = input("informe o operador(`+`, `-`, `*`, `/`):")

match operador:
    case "+":
        calculo = num1 + num2
        print(f"O resultado é: {calculo}")
    case "-":
        calculo = num1 - num2
        print(f"O resultado é: {calculo}")
    case "*":
        calculo = num1 * num2
        print(f"O resultado é: {calculo}")
    case "/":
        calculo = num1 / num2
        print(f"O resultado é: {calculo}")
    case _:
        print("Informação inválida!")